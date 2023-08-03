from django.urls import path

from . import views


app_name = "CRM"
urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login/", views.login_user, name="login"),
    path("auth/register/", views.register_user, name="register"),
]