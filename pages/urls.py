from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage_url, name='home-page'),
    path('blog', views.blog, name='blog-page')
]