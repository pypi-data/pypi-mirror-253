from django.urls import reverse
from wagtail.admin.panels import Panel

from .templatetags.feedback import (
    FEEDBACK_CSS,
    FEEDBACK_JS,
)


class FeedbackPanel(Panel):

    class BoundPanel(Panel.BoundPanel):
        template_name = "feedback/panels/feedback_panel.html"

        class Media:
            js = [
                FEEDBACK_JS,
                "wagtailadmin/js/date-time-chooser.js"
            ]
            css = {
                "all": [
                    FEEDBACK_CSS,
                ]
            }

        def is_shown(self):
            return super().is_shown() and self.request.user.has_perm("feedback.view_feedback")

        def get_context_data(self, parent_context=None):
            context = super().get_context_data(parent_context)
            context.update(
                self.panel.get_panel_context(self.instance)
            )
            return context
        
    @classmethod
    def get_panel_context(cls, instance, **kwargs):
        return {
            "page": instance,
            "panel_id": f"feedback-panel-{instance.pk}",
            "list_url": reverse("feedback_api", kwargs={"page_pk": instance.pk}),
            "chart_url": reverse("feedback_api_chart", kwargs={"page_pk": instance.pk}),
        }
