from django.shortcuts import render
from django.http import HttpResponseRedirect
from .form import StudentProjectForm


def getUserLogin(request):
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
    # db_object = StudentRegistration().objects.filter(studentId=username)
    # print(db_object)
    return True

def studentProjectOptions(request):
    stdForm = StudentProjectForm()
    return render(request,'ProjectSelection.html',stdForm)