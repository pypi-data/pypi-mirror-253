from django.shortcuts import (
    get_object_or_404,
    render,
)
from django.core.paginator import (
    Paginator,
)
from django.utils.translation import gettext_lazy as _
from django.http import (
    HttpResponse,
    JsonResponse,
)
import django_filters as filters
from wagtail.models import (
    Page,
)
from .. import (
    get_feedback_model,
)
from ..filters import (
    FeedbackAggregationFilter,
    FeedbackAggregationTypeFilter,
)
from ..panels import (
    FeedbackPanel,
)
from .utils import (
    redirect_or_respond,
    is_json_request,
    is_htmx_request,
    error,
)


Feedback = get_feedback_model()


PAGE_PARAM = "page"


class FeedbackDateRangeFilterSet(filters.FilterSet):
    created_at = filters.DateFromToRangeFilter(
        field_name="created_at",
        label=_("Creation Range"),
        help_text=_("The range of creation dates."),
    )

    class Meta:
        model = get_feedback_model()
        fields = [
            "created_at",
        ]

def feedback_api_aggregate(request, *args, **kwargs):
    if not request.user.has_perm("feedback.view_feedback"):
        return error(request, _("You do not have permission to view feedback instances."), to="wagtailadmin_home")
    
    page_qs = Page.objects.live().public().specific()
    page: Page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))

    if not page.permissions_for_user(request.user).can_edit():
        return error(request, _("You do not have permission to view feedback instances."), to="wagtailadmin_home")

    qs = Feedback.objects.select_related("page")
    qs = qs.filter(page=page)

    date_filter = FeedbackDateRangeFilterSet(request.GET, queryset=qs)
    qs = date_filter.qs

    filter_class = FeedbackAggregationTypeFilter
    if "period" not in request.GET:
        qs = qs.aggregate_percentage()
    filters = filter_class(request.GET, queryset=qs)
    qs = filters.qs

    filter_class = FeedbackAggregationFilter
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

    if is_json_request(request):
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
        return error(request, _("You do not have permission to view feedback instances."), to="wagtailadmin_home")
    
    page_qs = Page.objects.live().public().specific()
    page: Page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))

    if not page.permissions_for_user(request.user).can_edit():
        return error(request, _("You do not have permission to view feedback instances."), to="wagtailadmin_home")

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


    if is_json_request(request):
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
        return error(request, _("You do not have permission to view feedback instances."), to="wagtailadmin_home")
    
    qs = Feedback.objects.select_related("page")
    instance = get_object_or_404(qs, pk=kwargs.get("pk", None))

    if not instance.page.permissions_for_user(request.user).can_edit():
        return error(request, _("You do not have permission to view feedback instances."), to="wagtailadmin_home")
    
    if is_json_request(request):
        return JsonResponse({
            "success": True,
            "result": Feedback.serialize(instance),
        }, json_dumps_params={"indent": 2})

    return render(request, "feedback/panels/partials/feedback-list-item.html", {
        "feedback": instance,
    })


def feedback_api_delete(request, *args, **kwargs):
    if not request.user.has_perm("feedback.delete_feedback"):
        return error(request, _("You do not have permission to delete feedback instances."), to="wagtailadmin_home")
        
    if not request.method in ["POST", "DELETE", "GET"]:
        return error(request, _("You must use a POST, DELETE or GET request to delete feedback instances."), to="wagtailadmin_home")

    page_qs = Page.objects.live().public().specific()
    page: Page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))

    if not page.permissions_for_user(request.user).can_edit():
        return error(request, _("You do not have permission to delete feedback instances."), to="wagtailadmin_home")
    
    instance = get_object_or_404(Feedback, pk=kwargs.get("pk", None))

    if request.method == "GET":

        if is_json_request(request):
            return JsonResponse({
                "success": True,
                "result": Feedback.serialize(instance),
            }, json_dumps_params={"indent": 2})

        return render(request, "feedback/panels/partials/delete.html", {
            "feedback": instance,
            **FeedbackPanel.get_panel_context(page),
        })

    instance.delete()

    if is_htmx_request(request):
        return HttpResponse(content="", status=200)
    
    elif is_json_request(request):
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

