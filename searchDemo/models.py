from django.db import models
from django.urls.base import reverse

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, unique=True,) #, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=255, db_index=True, default='', unique=True,) #unique=True,
    slug = models.SlugField(null=True, blank=True, max_length=255, unique=True,) #, unique=True
    description = models.TextField(db_index=True)
    brand = models.CharField(db_index=True, max_length=255)
    category = models.CharField(db_index=True, max_length=255) #ForeignKey(Category, related_name='category')
    image = models.CharField(db_index=True, max_length=255)#ImageField(upload_to = 'product_images/', default = 'product_images/no-img.jpg')
    timestamp = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('product',
                       kwargs={'slug': self.slug})


    def __str__(self):
        return self.title

    
