from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("register/", views.register, name="register_page"),
    path("login/", auth_views.LoginView.as_view(template_name='user/login.html'), name="login_page"),
    path("logout/", auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout_page"),
    path("posts/", views.posts, name="posts_page"),
    path("profile/", views.profile, name="profile_page"),
]
