from django.shortcuts import render
from .forms import StudentRegistrationForm
from django.http import HttpResponseRedirect


def home(request):
    return render(request, 'Home.html')


def getUserLogin(request):
    if request.method == 'POST':
        print("Post Method Working Properly")
        username = request.POST['username']
        password = request.POST['password']
        if login(username, password):
            return render(request, 'StudentLoginForm.html')
    print("Something Went Wrong")
    return HttpResponseRedirect('/')


def login(username, password):
    if username != "" and password != "":
        return True
    else:
        return False


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
