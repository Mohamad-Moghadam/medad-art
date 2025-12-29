from rest_framework.serializers import ModelSerializer
from .models import Task

class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'progress', 'status', 'creator', 'assigned']
        extra_kwargs = {"progress" : {"read_only" : True}}