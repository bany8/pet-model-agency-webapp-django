from django.urls import path

from . import views

app_name = "user"
urlpatterns = [
    path("login/", views.login, name="login_page"),
    path("register/", views.register, name="register_page"),
    path("posts/", views.posts, name="posts_page"),
]
