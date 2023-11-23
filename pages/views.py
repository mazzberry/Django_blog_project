from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404

# Create your views here.


def blog(request):
    all_posts = Post.objects.all()
    context = {
        'posts':all_posts
    }
    return render(request, 'blog/post_list.html', context)

def post_detail_view(request, pk):
#    #find by given id
    post = get_object_or_404(Post, pk=pk)
#     try:
#         post = Post.objects.get(pk=pk)
#         print('id in url:', pk)

#     except Post.DoesNotExist :
#         context = None
#         print('ex')

    return render(request, 'blog/post_detail.html', {'post':post})
