from django.shortcuts import (
    get_object_or_404,
)
from django.utils.translation import gettext_lazy as _
from django.http import (
    HttpResponseNotAllowed,
)
from wagtail.models import (
    Page,
)
from .. import (
    get_feedback_model,
)
from .utils import (
    redirect_or_respond,
    error,
)


Feedback = get_feedback_model()
FeedbackForm = Feedback.get_form_class()


# Create your views here.
def feedback(request, *args, **kwargs):        
    if not request.method == "POST":
        return HttpResponseNotAllowed(["POST"])
    
    template = "feedback/form.html"

    page_qs = Page.objects.live().public().specific()
    page = get_object_or_404(page_qs, pk=kwargs.get("page_pk", None))
    form = Feedback.get_form_class()(
        request.POST,
        request=request,
        requires_message=False,
    )

    valid = form.is_valid()

    if valid:
        form.instance.page = page
        form.instance = form.save()
        # If the feedback is positive and it is allowed, or if it is negative
        # then show the message form.
        if hasattr(page, "allow_feedback_message_on_positive")\
            and not page.allow_feedback_message_on_positive()\
            and form.instance.positive\
            or not form.instance.positive:

            form = FeedbackForm(
                request=request,
                requires_message=True,
                instance=form.instance,
            )
        else:
            template = "feedback/thanks.html"
    else:
        template = "feedback/happy-sad.html"

    context = page.get_context(request, *args, **kwargs)
    context["form"] = form
    context["feedback"] = form.instance

    if form.errors:
        context["errors"] = form.errors

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

