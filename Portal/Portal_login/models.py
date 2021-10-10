from django.db import models

# Create your models here.
class StudentLogin(models.Model):
    username = models.CharField(max_length=10)
