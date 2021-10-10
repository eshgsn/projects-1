from django import forms

class StudentRegistrationForm(forms.Form):
    name = forms.CharField(max_length=50,empty_value=False)