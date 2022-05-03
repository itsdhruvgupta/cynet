from django.contrib import admin 
from django.urls import path
from home import views


urlpatterns = [
    path("/",views.index, name = "home"),
    path("/event_registration",views.event_registration, name= "event registration"),
    path("/winners",views.winners_page, name="winners")
]