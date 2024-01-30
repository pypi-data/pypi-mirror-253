from django.urls import path

from . import views

app_name = "feedback"

urlpatterns = [
    path("feedback/<int:page_pk>/", views.feedback, name="feedback"),
    path("feedback/<int:page_pk>/<int:pk>/", views.feedback_with_message, name="feedback_with_message"),
]

admin_urlpatterns = [
    path("feedback/api/<int:pk>/view/", views.feedback_api_view, name="feedback_api_detail"),
    path("feedback/api/<int:page_pk>/list/", views.feedback_api_list, name="feedback_api"),
    path("feedback/api/<int:page_pk>/chart/", views.feedback_api_aggregate, name="feedback_api_chart"),
    path("feedback/api/<int:page_pk>/delete/<int:pk>/", views.feedback_api_delete, name="feedback_api_delete"),
]

