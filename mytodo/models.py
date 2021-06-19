from django.db import models

# Create your models here.
class todoModel(models.Model):
    todo = models.CharField(max_length = 150)
    date = models.DateField(auto_now=False, auto_now_add=False)