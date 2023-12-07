from django.shortcuts import render, reverse, redirect
from django.http import HttpResponse
from .models import Post
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from .forms import newPostForm
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.


# def blog(request):
#     # all_posts = Post.objects.all()
#     all_posts = Post.objects.filter(status = 'pub').order_by('-datetime_modified')# ba "-..." gozashtan posht objecti ke
#     context = {                                                                   #mikhaym bar asas oon moratab beshe
#         'posts':all_posts                                                  #migim bar'aks moratab kon
#     }
#     return render(request, 'blog/post_list.html', context)
class PostListView(generic.ListView):

    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(status= 'pub').order_by(('-datetime_modified'))



# def post_detail_view(request, pk):
# #    #find by given id
#     post = get_object_or_404(Post, pk=pk)
# #     try:
# #         post = Post.objects.get(pk=pk)
# #         print('id in url:', pk)
#
# #     except Post.DoesNotExist :
# #         context = None
# #         print('ex')
#
#     return render(request, 'blog/post_detail.html', {'post':post})

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# def create_post_view(request):
#     if request.method == 'POST':
#         form = newPostForm(request.POST)
#         if form.is_valid():
#             form.save(True)
#             newPostForm()
#
#             return redirect(reverse('blog-page'))
#         pass
#     else:#get request
#         form = newPostForm()
#         pass
#     return render(request, 'blog/create_post.html', context={'form':form})

    # if request.method == 'POST':
    #     post_title = request.POST.get('title')
    #     post_text = request.POST.get('text')
    #
    #     user = User.objects.all()[0]
    #     Post.objects.create(title=post_title, text=post_text, author=user, status='pub')
    #
    # else:
    #     print('get req')
    # return render(request, 'blog/create_post.html')

class CreatePostView(generic.CreateView):
    form_class = newPostForm
    template_name = 'blog/create_post.html'

    pass

# def postUpdate(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     # post = Post.objects.get(pk=pk)
#
#     form = newPostForm(request.POST or None, instance=post)# neveshtan etelaat ghabli baray neshan dadan be user
#
#     if form.is_valid():
#         form.save()
#         return redirect(reverse('blog-page'))
#
#     return  render(request, 'blog/create_post.html', {'form':form})

class UpdatePostView(generic.UpdateView):
    model = Post
    # fields = ['title','text',.....] mitavanim jodagane field joda barayash benvisim vali ma form amade dar "forms.py" darim
    form_class = newPostForm
    template_name = 'blog/create_post.html'

# def delete_post_view(request, pk):
#     post= get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.delete()
#
#         return redirect(reverse('blog-page'))
#
#     return render(request, 'blog/post_delete.html',context={'post':post})

class DeletePostView(generic.DeleteView):

    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('blog-page')

    # def get_success_url(self):
    #     return reverse('blog-page')










