from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from agency.models import Advertisement


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "user/register.html", {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('user:login_page')
        return render(request, "user/register.html", {'form': form})


class PostsView(View):
    def get(self, request):
        context = Advertisement.objects.all()
        return render(request, "user/posts.html", context={'advertisements': context})


class ProfileView(LoginRequiredMixin, View):
    def get(self, request):
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        context = {
            'u_form': u_form,
            'p_form': p_form
        }

        return render(request, "user/profile.html", context)

    def post(self, request):
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account {username} updated!')
            return redirect('user:profile_page')
        else:
            context = {
                'u_form': u_form,
                'p_form': p_form
            }

            return render(request, "user/profile.html", context)
