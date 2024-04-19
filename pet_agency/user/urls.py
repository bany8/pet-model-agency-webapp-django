from django.contrib.auth import views as auth_views
from django.urls import path

from .views import RegisterView, PostsView, ProfileView

app_name = "user"
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register_page"),
    path("login/", auth_views.LoginView.as_view(template_name='user/login.html'), name="login_page"),
    path("logout/", auth_views.LogoutView.as_view(template_name='user/logout.html'), name="logout_page"),
    path("posts/", PostsView.as_view(), name="posts_page"),
    path("profile/", ProfileView.as_view(), name="profile_page"),
]
