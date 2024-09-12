from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=200)
    published_date = models.DateField()
    image = models.ImageField(upload_to='static/images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,
                                 related_name='Book', blank=True, null=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


@property
def image_url(self):
    return f'/media/{self.image}'

# Create your models here.
