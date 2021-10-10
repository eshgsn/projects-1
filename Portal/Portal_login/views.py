from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'Home.html')



def getUserLogin(request) :
    if request.method == 'POST':
        print("Post Method Working Properly")
        username = request.POST['username']
        password = request.POST['password']
        if login(username,password) == True:
            return render(request,'StudentLoginForm.html')
    print("Something Went Wrong")
    return render(request,'Home.html')



def login(username,password):
    if username != "" and password != "":
        return True
    else:
        return False
