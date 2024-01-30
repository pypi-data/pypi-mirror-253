from django.shortcuts import (
    get_object_or_404,
    redirect,
    render,
)
from django import forms
from django.contrib import messages as django_messages
from django.core.paginator import (
    Paginator,
)
from django.utils.translation import gettext_lazy as _
from django.http import (
    HttpResponse,
    HttpResponseNotAllowed,
    JsonResponse,
)
import django_filters as filters
from wagtail.models import (
    Page,
)
from . import (
    get_feedback_model,
)
from .filters import (
    FeedbackAggregationFilter,
)
from .forms import (
    FeedbackForm,
)
from .panels import (
    FeedbackPanel,
)

Feedback = get_feedback_model()

def redirect_or_respond(request, url, template, context=None, message_type = "success", message = None, *args, **kwargs):
    if context is None:
        context = {}

    if request.is_htmx:

        return render(
            request,
            template,
            context=context,
            *args,
            **kwargs,
        )

    if message:
        fn = getattr(django_messages, message_type)
        fn(request, message)

    return redirect(url)


def error(request, message, status=200, key = "error", *args, **kwargs):
    return render(request, "feedback/panels/partials/error.html", {
        key: message,
        **kwargs,
    }, status=status)


# Create your views here.
def feedback(request, *args, **kwargs):        
    if not request.method == "POST":
        return HttpResponseNotAllowed(["POST"])
    
    template = "feedback/form.html"

    page_qs = Page.objects.live().public().specific()
    page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))
    form = FeedbackForm(
        request.POST,
        request=request,
        requires_message=False,
    )

    valid = form.is_valid()

    if valid:
        form.instance.page = page
        form.instance = form.save()

    if hasattr(page, "allow_feedback_message_on_positive"):

        if (page.allow_feedback_message_on_positive() and form.instance.positive) or not form.instance.positive:
            form = FeedbackForm(
                request=request,
                requires_message=True,
                instance=form.instance,
            )
        else:
            template = "feedback/thanks.html"

    context = page.get_context(request, *args, **kwargs)
    context["form"] = form
    context["feedback"] = form.instance

    return redirect_or_respond(
        request,
        page.get_url(request),
        template,
        context=context,
        message=_("Thank you for your feedback."),
    )


def feedback_with_message(request, *args, **kwargs):
    if not request.method == "POST":
        return HttpResponseNotAllowed(["POST"])
    
    template = "feedback/form.html"

    page_qs = Page.objects.live().public().specific()
    page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))
    feedback = get_object_or_404(Feedback, pk=kwargs.get("pk", None))

    if hasattr(page, "allow_feedback_message_on_positive") \
        and not page.allow_feedback_message_on_positive() \
        and feedback.positive:
        return error(request, _("Feedback messages are not allowed on positive feedback."), WRAPPER="../wrapper.html")

    FeedbackForm = feedback.get_form_class()
    form = FeedbackForm(
        request.POST,
        instance=feedback,
        request=request,
        requires_message=True,
    )

    if form.is_valid():
        form.instance.page = page
        form.instance = form.save()
        template = "feedback/thanks.html"

    context = page.get_context(request, *args, **kwargs)
    context["form"] = form
    context["feedback"] = form.instance

    return redirect_or_respond(
        request,
        page.get_url(request),
        template,
        context=context,
    )


PAGE_PARAM = "page"


class FeedbackDateRangeFilterSet(filters.FilterSet):
    # creation_range_start = filters.DateTimeFilter(
    #     field_name="created_at",
    #     label=_("Creation Range Start"),
    #     help_text=_("The start of the range of creation dates."),
    #     widget=forms.DateInput(format="%d-%m-%Y"),
    #     lookup_expr="gte",
    # )
    # 
    # creation_range_end = filters.DateTimeFilter(
    #     field_name="created_at",
    #     label=_("Creation Range End"),
    #     help_text=_("The end of the range of creation dates."),
    #     widget=forms.DateInput(format="%d-%m-%Y"),
    #     lookup_expr="lte",
    # )

    created_at = filters.DateFromToRangeFilter(
        field_name="created_at",
        label=_("Creation Range"),
        help_text=_("The range of creation dates."),
    )

    class Meta:
        model = get_feedback_model()
        fields = [
            # "creation_range_start",
            # "creation_range_end",
            "created_at",
        ]

def feedback_api_aggregate(request, *args, **kwargs):
    if not request.user.has_perm("feedback.view_feedback"):
        return error(request, _("You do not have permission to view feedback instances."))
    
    page_qs = Page.objects.live().public().specific()
    page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))
    qs = Feedback.objects.select_related("page")
    qs = qs.filter(page=page)

    date_filter = FeedbackDateRangeFilterSet(request.GET, queryset=qs)
    qs = date_filter.qs

    filter_class = FeedbackAggregationFilter
    if "period" not in request.GET:
        qs = qs.aggregate_percentage()
    filters = filter_class(request.GET, queryset=qs)
    qs = filters.qs

    paginator = Paginator(qs, 5)
    page_number = request.GET.get(PAGE_PARAM, 1)
    page_obj = paginator.get_page(page_number)

    next = None
    if page_obj.has_next():
        query = request.GET.copy()
        query[PAGE_PARAM] = page_obj.next_page_number()
        next = f"{request.path}?{query.urlencode()}"

    previous = None
    if page_obj.has_previous():
        query = request.GET.copy()
        query[PAGE_PARAM] = page_obj.previous_page_number()
        previous = f"{request.path}?{query.urlencode()}"

    if request.is_json and request.accepts("application/json"):
        extra = {}

        if next:
            extra["next"] = next

        if previous:
            extra["previous"] = previous

        return JsonResponse({
            "success": True,
            "page": page_number,
            "pages": paginator.num_pages,
            "count": paginator.count,
            "results": list(page_obj.object_list),
            **extra,
        }, json_dumps_params={"indent": 2})

    return render(request, "feedback/panels/partials/aggregate.html", {
        "page": page,
        "queryset": qs,
        "filters": [
            date_filter,
            filters,
        ],
        "period": qs.period,
        "next": next,
        "previous": previous,
        "paginator": paginator,
        "page_obj": page_obj,
        "page_param": PAGE_PARAM,
        **FeedbackPanel.get_panel_context(page),
    })

def feedback_api_list(request, *args, **kwargs):
    if not request.user.has_perm("feedback.view_feedback"):
        return error(request, _("You do not have permission to view feedback instances."))
    
    page_qs = Page.objects.live().public().specific()
    page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))
    qs = Feedback.objects.select_related("page")
    qs = qs.filter(page=page)

    date_filter = FeedbackDateRangeFilterSet(request.GET, queryset=qs)
    qs = date_filter.qs

    filter_class = Feedback.get_filter_class()
    filters = filter_class(request.GET, queryset=qs)
    qs = filters.qs
    qs = qs.order_by("-created_at")

    paginator = Paginator(qs, 10)
    page_number = request.GET.get(PAGE_PARAM, 1)
    page_obj = paginator.get_page(page_number)

    next = None
    if page_obj.has_next():
        query = request.GET.copy()
        query[PAGE_PARAM] = page_obj.next_page_number()
        next = f"{request.path}?{query.urlencode()}"

    previous = None
    if page_obj.has_previous():
        query = request.GET.copy()
        query[PAGE_PARAM] = page_obj.previous_page_number()
        previous = f"{request.path}?{query.urlencode()}"


    if request.content_type == "application/json" and request.accepts("application/json"):
        extra = {}

        if next:
            extra["next"] = next

        if previous:
            extra["previous"] = previous

        return JsonResponse({
            "success": True,
            "page": page_number,
            "pages": paginator.num_pages,
            "count": paginator.count,
            "results": list(map(
                Feedback.serialize, page_obj.object_list,
            )),
            **extra,
        }, json_dumps_params={"indent": 2})
    
    return render(request, "feedback/panels/partials/list.html", {
        "page": page,
        "filters": [
            date_filter,
            filters,
        ],
        "paginator": paginator,
        "page_obj": page_obj,
        "next": next,
        "previous": previous,
        "page_param": PAGE_PARAM,
        **FeedbackPanel.get_panel_context(page),
    })

def feedback_api_view(request, *args, **kwargs):
    if not request.user.has_perm("feedback.view_feedback"):
        return error(request, _("You do not have permission to view feedback instances."))
    
    qs = Feedback.objects.select_related("page")
    instance = get_object_or_404(qs, pk=kwargs.get("pk", None))

    if request.content_type == "application/json" and request.accepts("application/json"):
        return JsonResponse({
            "success": True,
            "result": Feedback.serialize(instance),
        }, json_dumps_params={"indent": 2})

    return render(request, "feedback/panels/partials/feedback-list-item.html", {
        "feedback": instance,
    })

def feedback_api_delete(request, *args, **kwargs):
    if not request.user.has_perm("feedback.delete_feedback"):
        return error(request, _("You do not have permission to delete feedback instances."))
        
    if not request.method in ["POST", "DELETE", "GET"]:
        return error(request, _("You must use a POST, DELETE or GET request to delete feedback instances."))

    page_qs = Page.objects.live().public().specific()
    page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))
    instance = get_object_or_404(Feedback, pk=kwargs.get("pk", None))

    if request.method == "GET":

        if request.is_json:
            return JsonResponse({
                "success": True,
                "result": Feedback.serialize(instance),
            }, json_dumps_params={"indent": 2})

        return render(request, "feedback/panels/partials/delete.html", {
            "feedback": instance,
            **FeedbackPanel.get_panel_context(page),
        })

    instance.delete()

    if request.is_htmx:
        return HttpResponse(content="", status=200)
    
    elif request.is_json and request.accepts("application/json"):
        return JsonResponse({
            "success": True,
        }, json_dumps_params={"indent": 2})

    return redirect_or_respond(
        request,
        page.get_url(request),
        "feedback/thanks.html",
        context={
            "feedback": instance,
            **FeedbackPanel.get_panel_context(page),
        },
    )


