import random
import os
from django.db import models

# Create your models here.
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,3910209312)
    return

class Product(models.Model):  # make sure to name your models as singular
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=20, default=39.99)
    image = models.FileField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.title