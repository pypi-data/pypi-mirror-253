from django import forms
from django.db import models
from django.utils.translation import gettext_lazy as _
from typing import TYPE_CHECKING
from feedback import get_feedback_model

import django_filters as filters
import django_filters.widgets as filters_widgets
import django_filters.fields as filters_fields


if TYPE_CHECKING:
    from feedback.models import FeedbackQuerySet

class RangeWidget(filters_widgets.RangeWidget):
    widget_class = forms.NumberInput

    def __init__(self, attrs=None):
        widgets = (self.widget_class, self.widget_class)
        super(filters_widgets.RangeWidget, self).__init__(widgets, attrs)

class NumberRangeField(filters_fields.RangeField):
    widget = RangeWidget

    def compress(self, data_list):
        if data_list:
            return slice(*data_list)
        return None

class NumberRangeFilter(filters.NumericRangeFilter):
    field_class = NumberRangeField

class FeedbackAggregationFilter(filters.FilterSet):

    positivity_range = NumberRangeFilter(
        field_name="positive_percentage",
        label=_("Positivity Range"),
        help_text=_("The range of positivity to filter the results."),
        method="filter_positivity_range",
    )

    periods = filters.ChoiceFilter(
        label=_("Period"),
        help_text=_("The period to aggregate the feedback results."),
        empty_label=None,
        null_label=None,
        choices=[
            ("hour", _("Day/Hour")),
            ("date", _("Date")),
            ("month", _("Month")),
            ("year", _("Year")),
        ],
        method="filter_periods",
    )

    def filter_periods(self, queryset: "FeedbackQuerySet", name: str, value: str) -> "FeedbackQuerySet":
        return queryset.aggregate_percentage(date_arg=value)
    
    def filter_positivity_range(self, queryset: "FeedbackQuerySet", name: str, value: str) -> "FeedbackQuerySet":
        if not value:
            return queryset
        
        if value.start:
            queryset = queryset.filter(positive_percentage__gte=value.start)

        if value.stop:
            queryset = queryset.filter(positive_percentage__lte=value.stop)

        return queryset

class AbstractFeedbackFilter(filters.FilterSet):
    attitude = filters.ChoiceFilter(
        field_name="positive",
        label=_("Attitude"),
        empty_label=_("All"),
        help_text=_("The attitude of the feedback."),
        method="filter_attitude",
        choices=[
            (2, _("Positive")),
            (1, _("Negative")),
        ],
    )

    by_message = filters.ChoiceFilter(
        field_name="message",
        label=_("Has Message"),
        help_text=_("Whether the feedback has a message."),
        empty_label=_("All"),
        method="filter_has_message",
        choices=[
            (2, _("Yes")),
            (1, _("No")),
        ],
    )
    
    # period = filters.DateRangeFilter(
    #     field_name="created_at",
    #     label=_("Period"),
    #     help_text=_("The period the feedback was created."),
    # )

    class Meta:
        model = get_feedback_model()
        fields = [
            "attitude",
            # "period",
        ]

    def filter_attitude(self, queryset: "FeedbackQuerySet", name: str, value: bool) -> "FeedbackQuerySet":
        try:
            if int(value) == 2:
                return queryset.positive()
            elif int(value) == 1:
                return queryset.negative()
        except (ValueError, TypeError):
            pass
        
        return queryset.all()

    def filter_has_message(self, queryset: "FeedbackQuerySet", name: str, value: bool) -> "FeedbackQuerySet":
        try:
            if int(value) == 2:
                return queryset.filter(message__isnull=False).exclude(message__exact="")
            elif int(value) == 1:
                return queryset.filter(models.Q(message__isnull=True) | models.Q(message__exact=""))
        except (ValueError, TypeError):
            pass
        
        return queryset.all()
    