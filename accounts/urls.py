from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views
app_name= "accounts"

urlpatterns = [

    path("login/",views.log_in,name="login"),
	path("signup/",views.sign_up,name = "signup"),
    #path("signup/",views.sign_up,name="signup"),
    path("logout/",views.log_out,name="logout"),
    path("profile",views.profile,name="profile"),
        path("update",views.update,name="update"),


]
