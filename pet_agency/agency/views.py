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


class AdvertisementListView(ListView):
    model = Advertisement
    template_name = 'agency/gallery.html'
    context_object_name = 'advertisements'
    ordering = ['-date_posted']
    paginate_by = 2


class AdvertisementDetailView(DetailView):
    model = Advertisement


class AdvertisementCreateView(LoginRequiredMixin, CreateView):
    model = Advertisement
    fields = ['name', 'age', 'breed', 'description']

    def form_valid(self, form):
        form.instance.owner_id = self.request.user.id
        return super().form_valid(form)


class AdvertisementUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Advertisement
    fields = ['name', 'age', 'breed', 'description']

    def test_func(self):
        adv = self.get_object()
        if self.request.user == adv.owner:
            return True
        return False


class AdvertisementDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Advertisement
    success_url = '/gallery'

    def test_func(self):
        adv = self.get_object()
        if self.request.user == adv.owner:
            return True
        return False
