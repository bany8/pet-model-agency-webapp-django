from django.db import models
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = PhoneNumberField(blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics', max_length=200)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 200 or img.width > 200:
            output_size = (200, 200)
            img.thumbnail(output_size)
            img.save(self.image.path)
