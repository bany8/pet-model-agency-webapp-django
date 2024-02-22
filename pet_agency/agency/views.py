from django.shortcuts import render


def home(request):
    return render(request, "agency/home.html")


def gallery(request):
    return render(request, "agency/gallery.html")
