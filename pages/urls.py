from turtle import home
from django.urls import path
from .views import HomePageView,AboutPageView,SigninPageView


urlpatterns = [
    path('',HomePageView.as_view() , name= 'home'),
    path('about/',AboutPageView.as_view() , name= 'about'),
    path('Signin/',SigninPageView.as_view() , name= 'Signin'),

]