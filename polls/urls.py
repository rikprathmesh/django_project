from django.urls import path
from . import views


urlpatterns = [

    path('', views.login, name='login'),
    path("booking", views.booking1, name="booking1"),
    path("index", views.index, name="index"),
    path("registration1", views.registration1, name="registration1"),
    path("menu", views.menu1, name="menu")



]
