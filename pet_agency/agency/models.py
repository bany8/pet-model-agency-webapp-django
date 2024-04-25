from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User

from PIL import Image


class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100, default="")
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    adv_pic = models.ImageField(default='default_adv.jpg', upload_to='adv_pics', max_length=200)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('agency:adv_page', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        super(Advertisement, self).save(*args, **kwargs)

        img = Image.open(self.adv_pic.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.adv_pic.path)
