from django.urls import path
from . import views


urlpatterns = [
    path('signup', views.signup_view.as_view(), name='signup'),

]