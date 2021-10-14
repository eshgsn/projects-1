from . import views
from django.urls import path

urlpatterns = [
    path('', views.home,name='home'),
    path('getUserLogin',views.getUserLogin,name='getUserLogin'),
    path('StudentForm',views.StudentForm,name='StudentForm'),
    path('StudentLoginFormSubmit',views.StudentLoginFormSubmit,name='StudentLoginFormSubmit')
]