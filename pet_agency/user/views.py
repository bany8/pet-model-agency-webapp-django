from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import logout as logout_user
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from agency.models import Advertisement


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


class UserAdvertisementListView(ListView):
    model = Advertisement
    template_name = 'user/posts.html'
    context_object_name = 'advertisements'
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Advertisement.objects.filter(owner=user).order_by('-date_posted')


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            username = u_form.cleaned_data.get('username')
            messages.success(request, f'Account {username} updated!')
            return redirect('user:profile_page')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "user/profile.html", context)
