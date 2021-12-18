from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponseRedirect
from StudentLogin.forms import StudentRegistrationForm
from .form import StudentProjectForm

def home(request):
    return render(request, 'Home.html')

def about(request):
    return render(request,'about.html')


def StudentForm(request):
    makeform = StudentRegistrationForm()
    return render(request, 'StudentLoginForm.html', {'form': makeform})



def OnClickProjectSubmittion(request):
    if request.method == 'POST':
        print("Working")
        sub = StudentProjectForm(request.POST)
        if sub.is_valid():
            sub.save()
        messages.info(request,"Successfully Done...")
        return HttpResponseRedirect('/')
    return render(request,'Home.html')



def StudentLoginFormSubmit(request):
    makeform = StudentRegistrationForm()
    if request.method == 'POST':
        forms = StudentRegistrationForm(request.POST)
        if forms.is_valid():
            forms.save()
            print("Data Values are Saved")
        return render(request, 'Home.html')
    return render(request, 'StudentLoginForm.html', {'form', makeform})