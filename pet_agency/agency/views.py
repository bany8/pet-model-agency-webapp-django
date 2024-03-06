from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Advertisement


def home(request):
    return render(request, "agency/home.html")


class AdvertismentListView(ListView):
    model = Advertisement
    template_name = 'agency/gallery.html'
    context_object_name = 'advertisements'
    ordering = ['date_posted']


class AdvertismentDetailView(DetailView):
    model = Advertisement


class AdvertismentCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    fields = ['name', 'age', 'breed', 'description']

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class AdvertismentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    fields = ['name', 'age', 'breed', 'description']

    def test_func(self):
        adv = self.get_object()
        if self.request.user == adv.owner:
            return True
        return False


class AdvertismentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertisement
    success_url = '/gallery'

    def test_func(self):
        adv = self.get_object()
        if self.request.user == adv.owner:
            return True
        return False
