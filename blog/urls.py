from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='posts'),
    path('post/<int:post_id>/<slug:slug>/', views.post_detail, name='post-detail'),
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<slug:slug>/', views.posts_by_tag, name='posts-by-tag'),
]