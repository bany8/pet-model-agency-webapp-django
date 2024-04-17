from django.urls import path
from .views import (
    HomePage,
    AdvertismentListView,
    AdvertismentDetailView,
    AdvertismentCreateView,
    AdvertismentUpdateView,
    AdvertismentDeleteView
)
from . import views

app_name = "agency"
urlpatterns = [
    path("", HomePage.as_view(), name="home_page"),
    path("gallery/", AdvertismentListView.as_view(template_name='agency/gallery.html'), name="gallery_page"),
    path("adv/<int:pk>/", AdvertismentDetailView.as_view(template_name='agency/adv.html'), name="adv_page"),
    path("adv/<int:pk>/update/", AdvertismentUpdateView.as_view(template_name='agency/adv_create_edit.html'), name="adv_update_page"),
    path("adv/<int:pk>/delete/", AdvertismentDeleteView.as_view(template_name='agency/adv_delete.html'), name="adv_delete_page"),
    path("adv/create/", AdvertismentCreateView.as_view(template_name='agency/adv_create_edit.html'), name="adv_create_page")
]
