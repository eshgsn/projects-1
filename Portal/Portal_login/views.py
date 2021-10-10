from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'Home.html')

def getUserLogin(request):
    if request.method == 'POST':
        print("Working Properly")
        username = request.POST['username']
        password = request.POST['password']
        return HttpResponse("<h1>Working</h1>" + username + " " + password)
    print("Something Went Wrong")
    return render(request,'Home.html')
