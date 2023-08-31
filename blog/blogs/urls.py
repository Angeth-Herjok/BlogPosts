from django.urls import path
from .views import blog_post_list, blog_post_detail

urlpatterns = [
    path('', blog_post_list, name='post-list'),
    path('posts/<int:pk>/', blog_post_detail, name='post-detail'),
]