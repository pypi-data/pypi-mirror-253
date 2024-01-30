from typing import Callable, TYPE_CHECKING, Type
from django.http import HttpRequest
from wagtail.models import Page
from .options import (
    FEEDBACK_DUPLICATE_CHECK,
    IS_PROXIED,
)

from . import get_feedback_model


Feedback = get_feedback_model()

if TYPE_CHECKING:
    from feedback.models import AbstractFeedback
    from feedback.forms import FeedbackForm

# before_feedback_form_valid
# after_feedback_form_valid
# before_feedback_message_form_valid
# after_feedback_message_form_valid
    
class Feedbackend:
    def __init__(self, request: HttpRequest, page: Page, form: FeedbackForm):
        self.request = request
        self.page = page
        self.form = form

    def check_duplicate(self, initial_form = False) -> bool:
        raise NotImplementedError("This method must be implemented by a subclass.")

    def finish(self, instance: "AbstractFeedback") -> None:
        raise NotImplementedError("This method must be implemented by a subclass.")
    
    def save(self, commit: bool = True) -> "AbstractFeedback":
        instance = self.form.save(commit=False)
        instance.page = self.page
        if commit:
            instance.save()

        self.finish(instance)
        return instance

def get_ip_address(request: HttpRequest):
    if IS_PROXIED:
        addr: str = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if addr:
            return addr.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR', None)

def check_duplicate_ip(request: HttpRequest, form: FeedbackForm) -> bool:
    if not request:
        raise RuntimeError("A request must be passed to the form when the instance does not have an IP address.")
    
    ip_address = get_ip_address(request)
    feedback_qs = Feedback.objects.filter(
        ip_address=ip_address,
        page=form.page,
    )
    
    return feedback_qs.exists()


def check_none(request: HttpRequest, form: FeedbackForm) -> bool:
    return False


def check_duplicate_session(request: HttpRequest, form: FeedbackForm) -> bool:
    if not request:
        raise RuntimeError("A request must be passed to the form when the instance does not have an IP address.")
    
    key = f"user-feedback-{form.page.pk}"

    return key in request.session



_Funcs: dict[str, Callable[[HttpRequest, Page], bool]] = {
    "ip_address": setup_ip_check,
    "session": setup_session_check,
}

is_duplicate = _Funcs.get(FEEDBACK_DUPLICATE_CHECK, check_none)

