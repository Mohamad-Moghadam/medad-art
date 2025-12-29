from django.db import models

class Tasks(models):
    title = models.CharField(max_length= 50)
    description= models.TextField(blank= True, null= True)
    