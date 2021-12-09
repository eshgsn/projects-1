from django.shortcuts import render
from .forms import StudentRegistrationForm
from django.http import HttpResponseRedirect
from .models import StudentRegistration

def home(request):
    return render(request, 'Home.html')


def StudentForm(request):
    makeform = StudentRegistrationForm()
    return render(request, 'StudentLoginForm.html', {'form': makeform})


def StudentLoginFormSubmit(request):
    makeform = StudentRegistrationForm()
    if request.method == 'POST':
        forms = StudentRegistrationForm(request.POST)

        if forms.is_valid():
            forms.save()
            print("Data Values are Saved")
        return render(request, 'Home.html')
    return render(request, 'StudentLoginForm.html', {'form', makeform})
