from django.urls import path

from . import views

app_name="User"
urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.loginPage, name="login"),
    path("logout/", views.logoutPage, name="logout"),
    path("register/", views.registrationPage, name="register"),
    path("profile", views.profile, name="profile"),
]
