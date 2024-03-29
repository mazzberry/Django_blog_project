from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    STATUS_CHOICES = (
        ('pub','published'),
        ('drf','draft'),
    )

    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE) # app auth ->  Table user
    datetime_created = models.DateTimeField(auto_now_add=True)
    datetime_modified = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES , max_length=3)

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):#mohem va tamrin shavad baz...
        return reverse('post-detail',args=[self.id]) #PISHBINI url daryafti baray namayesh object dar site

