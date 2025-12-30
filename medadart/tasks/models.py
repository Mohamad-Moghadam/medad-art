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

    def save(self, *args, **kwargs):

        if self.progress == 0 and self.status != self.TODO:
            self.status = self.TODO
        elif self.progress == 100 and self.status != self.COMPLETED:
            self.status = self.COMPLETED
        elif 0 < self.progress < 100 and self.status not in [self.IN_PROGRESS]:
            self.status = self.IN_PROGRESS

        if self.status == self.TODO and self.progress != 0:
            self.progress = 0
        elif self.status == self.COMPLETED and self.progress != 100:
            self.progress = 100
        elif self.status == self.IN_PROGRESS and (self.progress == 0 or self.progress == 100):
            self.progress = 1

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
