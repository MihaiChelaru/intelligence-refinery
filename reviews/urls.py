from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', TemplateView.as_view(template_name='reviews/review_home.html'), name='reviews-home'),
    path('courses/', views.course_list, name='courses'),
    path('books/', views.book_list, name='books'),
    path('software/', views.software_list, name='software'),
    path('<int:pk>/<slug:slug>/', views.review_detail, name='review-detail'),
]