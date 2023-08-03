from django.urls import path

from . import views


app_name = "CRM"
urlpatterns = [
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("auth/login/", views.login_user, name="login"),
]