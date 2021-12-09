from . import views
from django.urls import path


urlpatterns = [
    path('getUserLogin',views.getUserLogin,name='getUserActivity'),
    path('selectProject', views.studentProjectOptions,name='home'),
]