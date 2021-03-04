from django.urls import path
from . import views


app_name = "topic"

urlpatterns = [
    path("", views.TopicListView.as_view(), name="list"),
    path("<slug:slug>/", views.TopicDetailView.as_view(), name="detail"),

]