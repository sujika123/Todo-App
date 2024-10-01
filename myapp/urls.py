
from django.urls import path

from myapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('userhome', views.userhome, name='userhome'),
    path('log', views.log, name='log'),
    path('register/',views.register,name='register'),
    path('profileview', views.profileview, name='profileview'),
    path('profileupdate/<int:id>/',views.profileupdate,name='profileupdate'),
    path('addevent', views.addevent, name='addevent'),
    path('viewevent', views.viewevent, name='viewevent'),
    path('eventupdate/<int:id>/', views.eventupdate, name='eventupdate'),
    path('eventdelete/<int:id>/', views.eventdelete, name='eventdelete'),

    ]