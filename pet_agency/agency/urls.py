from django.urls import path
from .views import (
    AdvertismentListView,
    AdvertismentDetailView,
    AdvertismentCreateView,
    AdvertismentUpdateView,
    AdvertismentDeleteView
)
from . import views

app_name = "agency"
urlpatterns = [
    path("", views.home, name="home_page"),
    path("gallery/", AdvertismentListView.as_view(), name="gallery_page"),
    path("adv/<int:pk>/", AdvertismentDetailView.as_view(), name="adv_page"),
    path("adv/<int:pk>/update/", AdvertismentUpdateView.as_view(), name="adv_update_page"),
    path("adv/<int:pk>/delete/", AdvertismentDeleteView.as_view(), name="adv_delete_page"),
    path("adv/create/", AdvertismentCreateView.as_view(), name="adv_create_page")
]
