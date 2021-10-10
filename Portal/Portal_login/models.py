from django.db import models

# Create your models here.
class StudentLogin(models.Model):
    username = models.CharField(
        max_length=10,blank=False,null=False
    )
    password = models.CharField(
        max_length=15, blank=False, null=False
    )

    def __str__(self):
        return self.username

