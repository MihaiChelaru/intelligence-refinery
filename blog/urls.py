from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.post_list, name='posts'),
    path('post/<int:post_id>/<slug:slug>/', views.post_detail, name='post-detail'),
]