from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def logout(request):
    logout_user(request)
    return redirect('user:login_page')


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user:login_page')
    else:
        form = UserRegisterForm()
    return render(request, "user/register.html", {'form': form})


@login_required
def posts(request):
    return render(request, "user/posts.html")


@login_required
def profile(request):
    return render(request, "user/profile.html")
