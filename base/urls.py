from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name="index"),
    path('home/',views.home,name="home"),
    path('about/', views.about, name="about"),
    path('studio/', views.studio, name="studio"),
    path('blog/', views.blog, name="blog"),
    path('contact/',views.contact,name="contact"),
    path('photo/<str:pk>/',views.photo,name="photo"),
    path('design/', views.design, name="design"),
    path('doodlemotion/', views.video, name="motion"),
    path('doodledesign/', views.designd, name="doodledesign"),
    path('doodlebites/', views.bite, name="doodlebites"),


    path('send_email/',views.sendEmail,name="send_email"),


]

