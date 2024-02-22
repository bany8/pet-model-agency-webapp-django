from django.urls import path

from . import views

app_name = "agency"
urlpatterns = [
    path("", views.home, name="home_page")
]
