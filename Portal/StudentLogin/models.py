from django.db import models

# Create your models here.
class StudentRegistration(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    studentId = models.IntegerField(null=False, blank=False)
    password = models.CharField(max_length=20, null=False, blank=False)
    gender_choices = [
        ('male', "Male"),
        ("female", "Female"),
    ]
    gender = models.CharField(
        max_length=6, blank=False, null=False,
        choices=gender_choices,
    )
    date_of_birth = models.DateField(blank=False, null=False)

    phone_number = models.IntegerField(blank=False, null=False)

    email = models.EmailField(max_length=100, blank=False, null=False, unique=True)

    course = models.CharField(
        max_length=6, blank=False, null=False
    )
    sem_choice = [
        ('1st',"first"), ('2nd','second'), ('3rd','third'), ('4th','forth'),
        ('5nd','fifth'), ('6th','sixth'), ('7th','seventh'), ('8th','eighth')
    ]
    semester = models.CharField(
        max_length=3, null=False, blank=False,
        choices=sem_choice
    )
    yearOfAdmission = models.DateField(blank=False,null=False)
    yearOfPassout = models.DateField(blank=False,null=False)

    def __str__(self):
        return self.name
