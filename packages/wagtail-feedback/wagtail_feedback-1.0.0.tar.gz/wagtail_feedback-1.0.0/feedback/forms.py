from typing import Any
from django import forms
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from . import models, get_feedback_model


is_proxied = getattr(settings, "USE_X_FORWARDED_HOST", False)

def get_ip_address(request):
    if is_proxied:
        addr = request.META.get('HTTP_X_FORWARDED_FOR', None)
        if addr:
            return addr.split(',')[-1].strip()
    else:
        return request.META.get('REMOTE_ADDR', None)


class AbstractFeedbackForm(forms.ModelForm):
    class Meta:
        model = get_feedback_model()
        fields = [
            "positive",
            "message",
        ]

        widgets = {
            "message": forms.Textarea(attrs={
                "placeholder": _("Message"),
                "rows": 3,
            }),
        }

        help_texts = {
            "message": _("What would you like to see improved?"),
        }
    
    def __init__(self, *args, request=None, requires_message = True, **kwargs):
        self.request = request
        self.requires_message = requires_message
        super().__init__(*args, **kwargs)
        if self.requires_message:
            del self.fields["positive"]
            self.fields["message"].required = True
        else:
            del self.fields["message"]
    
    def clean(self):
        cleaned = super().clean()
        if self.requires_message:
            message = cleaned.get("message", "")
            if not message.strip():
                raise ValidationError(_("You must provide a message."))
        
        return cleaned

class FeedbackForm(AbstractFeedbackForm):
    def save(self, commit: bool = True) -> Any:
        instance = super().save(False)
        if not self.request and not instance.ip_address:
            raise RuntimeError("A request must be passed to the form when the instance does not have an IP address.")

        elif self.request and not instance.ip_address:
            instance.ip_address = get_ip_address(self.request)

        if commit:
            instance.save()

        return instance
    


