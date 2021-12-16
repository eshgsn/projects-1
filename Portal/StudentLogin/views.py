from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistrationForm
from .models import StudentRegistration

def getUserLogin(request) -> (HttpResponseRedirect or HttpResponse):
    if request.method == 'POST':
        print("Post Method Working Properly")
        username = request.POST['username']
        password = request.POST['password']
        formStd = StudentProjectForm()
        if login(username, password):
            return render(request, 'ProjectSelection.html',{'form': formStd})
    print("Something Went Wrong")
    return HttpResponseRedirect('/')


def login(username, password) -> bool:
    db_object = StudentRegistration.objects.all()
    print(db_object)
    return True

def studentProjectOptions(request) -> HttpResponse:
    stdForm = StudentProjectForm()
    return render(request,'ProjectSelection.html',stdForm)