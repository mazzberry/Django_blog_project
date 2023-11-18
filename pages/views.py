from django.shortcuts import render
from .models import Post

# Create your views here.

def homepage_url(request):
    context={
        'page-id':'home page',
    }
    return render(request, 'home_page/home.html',context)

def blog(request):
    all_posts = Post.objects.all()
    context = {
        'all_p':all_posts
    }

    return render(request, 'home_page/blog.html',context)