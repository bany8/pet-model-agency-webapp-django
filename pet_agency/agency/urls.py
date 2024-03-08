from django.urls import path
from .views import (
    AdvertisementListView,
    AdvertisementDetailView,
    AdvertisementCreateView,
    AdvertisementUpdateView,
    AdvertisementDeleteView
)
from . import views

app_name = "agency"
urlpatterns = [
    path("", views.home, name="home_page"),
    path("gallery/", AdvertisementListView.as_view(), name="gallery_page"),
    path("adv/<int:pk>/", AdvertisementDetailView.as_view(), name="adv_page"),
    path("adv/<int:pk>/update/", AdvertisementUpdateView.as_view(), name="adv_update_page"),
    path("adv/<int:pk>/delete/", AdvertisementDeleteView.as_view(), name="adv_delete_page"),
    path("adv/create/", AdvertisementCreateView.as_view(), name="adv_create_page")
]
