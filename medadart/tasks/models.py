from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    TODO = "TODO"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"

    STATUS_CHOICES = [(TODO, "To Do"), (IN_PROGRESS, "In Progress"), (COMPLETED, "Completed")]
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    progress = models.PositiveSmallIntegerField(default=0, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES ,default=TODO)

    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="created_tasks")

    assigned = models.ForeignKey(User, on_delete=models.CASCADE, related_name="assigned_tasks")

    def __str__(self):
        return self.title
