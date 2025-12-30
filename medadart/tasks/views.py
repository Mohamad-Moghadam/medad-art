from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import TaskSerializer
from .models import Task
from django.db import models
from django.db.models import Q


class NewTask(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class ChangeProgression(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(models.Q(creator=self.request.user) | models.Q(assigned=self.request.user))

    def perform_update(self, serializer):
        task = serializer.instance
        data = serializer.validated_data

        status_sent = "status" in data
        progress_sent = "progress" in data

        task = serializer.save()

        if status_sent:
            if task.status == Task.TODO:
                task.progress = 0
            elif task.status == Task.IN_PROGRESS:
                if task.progress == 0:
                    task.progress = 1
            elif task.status == Task.COMPLETED:
                task.progress = 100

        elif progress_sent:
            if task.progress == 0:
                task.status = Task.TODO
            elif 0 < task.progress < 100:
                task.status = Task.IN_PROGRESS
            elif task.progress == 100:
                task.status = Task.COMPLETED

        task.save()

class DeleteTask(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user)