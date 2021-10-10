from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'Home.html')

def getUserLogin(request):
    # if request.methord == 'post':
    #     pass
    username = request.POST['username']
    password = request.POST['password']
    print("Hello This is")
    return HttpResponse("<h1>Working</h1>"+username+" "+password)
