from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100, default="")
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agency:adv_page', kwargs={'pk': self.pk})
