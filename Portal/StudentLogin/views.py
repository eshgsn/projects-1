from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from StudentProjectData.form import StudentProjectForm
from .models import StudentRegistration
from django.contrib import messages

def getUserLogin(request) -> (HttpResponseRedirect or HttpResponse):
    if request.method == 'POST':
        print("Post Method Working Properly")
        username = request.POST['username']
        password = request.POST['password']
        formStd = StudentProjectForm()
        if login(username, password):
            print("Authentication Successfully...")
            messages.info(request,"Successfully Login")
            return render(request, 'ProjectSelection.html',{'form': formStd})
    messages.info(request,"User Id or Password is Incorrect")
    print("Authentication failed!!!")
    return HttpResponseRedirect('/')


def login(username, password) -> bool:
    db_object = StudentRegistration.objects.all()
    for i in db_object:
        print(f" geting Id {username} and pass {password} || data from DB id {i.studentId} and pass {i.password}")
        if i.studentId==int(username) and i.password==password:
            print("userId and Password Found")
            return True
    print("userId and Password Not Found")
    return False

def studentProjectOptions(request) -> HttpResponse:
    stdForm = StudentProjectForm()
    return render(request,'ProjectSelection.html',stdForm)