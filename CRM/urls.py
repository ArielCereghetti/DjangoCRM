from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


app_name = "CRM"
urlpatterns = [
    path("", views.index, name="index"),
    path("auth/login/", views.login_user, name="login"),
    path("auth/logout/", auth_views.LogoutView.as_view(next_page='CRM:login'), name="logout"),
    path("auth/register/", views.register_user, name="register"),
]