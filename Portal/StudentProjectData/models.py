from django.db import models

# Create your models here.
class StudentLogin(models.Model):
    name = models.CharField(
        max_length=10,blank=False,null=False
    )
    studentId = models.CharField(
        max_length=15, blank=False, null=False
    )
    projectChoose = models.CharField(
        max_length=30,blank=False,null=False
    )

    def __str__(self):
        return self.username

