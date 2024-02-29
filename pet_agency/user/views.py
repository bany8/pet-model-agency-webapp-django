from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def login(request):
    return render(request, "user/login.html")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('agency:home_page')
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {'form': form})


def posts(request):
    return render(request, "user/posts.html")
