from django.shortcuts import render
from .models import Post

# Create your views here.

def homepage_url(request):
    context={
        'page-id':'home page',
    }
    return render(request, '_base.html',context)

def blog(request):
    all_posts = Post.objects.all()
    context = {
        'all_p':all_posts
    }
################# temp name nazashti
    return render(request, 'blog.blog.html',context)