from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'blog'

#TODO: refactor posts-by-tag as a site-wide view that displays color-coded cards that link to blog posts or reviews

urlpatterns = [
    path('', views.post_list, name='posts'),
    path('post/<int:post_id>/<slug:slug>/', views.post_detail, name='post-detail'),
    path('revealjs/', TemplateView.as_view(template_name='blog/revealjs.html'), name='revealjs'),
    path('sql-intro/', TemplateView.as_view(template_name='blog/intro_to_sql.html'), name='sql-intro'),
]