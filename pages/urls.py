from django.urls import path
from . import views


urlpatterns = [
   # path('', views.homepage_url, name='home-page'),
    path('', views.PostListView.as_view(), name='blog-page'),
    path('<int:pk>/', views.PostDetailView.as_view() , name='post-detail'),
    path('createp/', views.CreatePostView.as_view(), name = 'new-post'),
    path('<int:pk>/update/', views.UpdatePostView.as_view(), name = 'update-post'),
    path('<int:pk>/delete', views.DeletePostView.as_view(), name= 'delete-post')
]