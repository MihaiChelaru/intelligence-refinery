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
    path('contact/', views.contact, name='contact'),
    path('success/', TemplateView.as_view(template_name='blog/success.html'), name='success'),
    path('course_reviews/', TemplateView.as_view(template_name='blog/course_reviews.html'), name='course-reviews'),
    path('portfolio/', TemplateView.as_view(template_name='blog/portfolio.html'), name='portfolio'),
    path('revealjs/', TemplateView.as_view(template_name='blog/revealjs.html'), name='revealjs'),
    path('sql_intro/', TemplateView.as_view(template_name='blog/intro_to_sql.html'), name='sql-intro'),
]