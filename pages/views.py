from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.


def blog(request):
    all_posts = Post.objects.all()
    context = {
        'posts':all_posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail_view(request, pk):
#    #find by given id
    post = Post.objects.get(pk=pk)
    print('id in url:', pk)

    return render(request, 'blog/post_detail.html', {'post':post})
