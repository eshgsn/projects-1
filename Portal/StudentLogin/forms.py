from django import forms
from .models import StudentRegistration


class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'studentId': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'required': 'True'}),
            'gender' : forms.Select(attrs={'class': 'form-control', 'required': 'True'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'required': 'True', 'type':'date'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control', 'required': 'True'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'required': 'True'}),
            'course': forms.TextInput(attrs={'class': 'form-control', 'required': 'True'}),
            'semester': forms.Select(attrs={'class': 'form-control', 'required': 'True'}),
            'yearOfAdmission': forms.DateInput(attrs={'class': 'form-control', 'required':'True', 'type':'date'}),
            'yearOfPassout': forms.DateInput(attrs={'class': 'form-control', 'required': 'True', 'type':'date'}),
        }
        labels = {
            'name': 'Student Name:',
            'studentId': 'Student Id:',
            'password': 'Set Password:',
            'gender' : 'Gender',
            'date_of_birth': 'Date Of Birth:',
            'phone_number': 'Student Mobile Number:',
            'email': 'Student Email:',
            'course': 'Course:',
            'semester':'Semester',
            'yearOfAdmission': 'Year Of Admission',
            'yearOfPassout': 'Year Of Pass Out'
        }