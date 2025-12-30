from django.urls import path
from .views import NewTask, ChangeProgression
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("token/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("create/", NewTask.as_view()),
    path("update/<int:pk>/", ChangeProgression.as_view()),
]
