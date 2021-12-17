from django.shortcuts import render
from StudentLogin.forms import StudentRegistrationForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'Home.html')

def about(request):
    return render(request,'about.html')


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