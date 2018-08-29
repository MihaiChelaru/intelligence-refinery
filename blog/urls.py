from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='posts'),
    path('post/<int:post_id>/<slug:slug>/', views.post_detail, name='post-detail'),
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<slug:slug>/', views.posts_by_tag, name='posts-by-tag'),
    path('resources/', views.resources, name='resources'),
    path('revealjs/', TemplateView.as_view(template_name="72hr_HR_revealjs.html"), name='revealjs'),
]