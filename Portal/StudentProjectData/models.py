from django.db import models

# Create your models here.
class StudentProjectModel(models.Model):
    name = models.CharField(
        max_length=30,blank=False,null=False
    )
    studentId = models.CharField(
        max_length=15, blank=False, null=False
    )

    Topic_list = [
        ('Topic1' , 'topic1')
    ]

    projectChoose = models.CharField(
        max_length=30,blank=False,null=False,
        choices=Topic_list
    )

    def __str__(self):
        return self.username

