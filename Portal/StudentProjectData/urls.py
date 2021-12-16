from django.conf.urls import include
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home,name='home'),
    path('StudentForm',views.StudentForm,name='StudentForm'), #File Path
    path('StudentLoginFormSubmit',views.StudentLoginFormSubmit,name='StudentLoginFormSubmit'), #action Function
    path('',include('StudentProjectData.urls')) #module include path
]