from django.shortcuts import render


def login(request):
    return render(request, "user/login.html")


def register(request):
    return render(request, "user/register.html")


def posts(request):
    return render(request, "user/posts.html")