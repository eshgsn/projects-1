from django.conf.urls import include
from . import views
from django.urls import path,include

urlpatterns = [
    path('', views.home,name='home'),
    path('about',views.about,name='about'),
    path('StudentForm',views.StudentForm,name='StudentForm'), #File Path
    path('OnClickProjectSubmittion', views.OnClickProjectSubmittion,name='OnClickProjectSubmittion'),
    path('StudentLoginFormSubmit',views.StudentLoginFormSubmit,name='StudentLoginFormSubmit'), #action Function
    path('',include('StudentLogin.urls')) #module include path
]