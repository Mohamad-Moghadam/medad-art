from django.urls import path
from .views import NewTask, ChangeProgression

urlpatterns = [
    path("create/", NewTask.as_view()),
    path("update/", ChangeProgression.as_view()),
]
