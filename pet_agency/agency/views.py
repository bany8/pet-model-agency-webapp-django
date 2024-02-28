from django.shortcuts import render
from .models import Advertisement


def home(request):
    return render(request, "agency/home.html")


def gallery(request):
    context = {"advertisements": Advertisement.objects.all()}
    return render(request, "agency/gallery.html", context)
