from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from PIL import Image


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    country = models.CharField(max_length=120, default='Country')
    city = models.CharField(max_length=120, default='City')
    birthday = models.DateField(default=datetime.strptime("01/01/1900", "%d/%m/%Y"))

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size)
            img.save(self.image.path)