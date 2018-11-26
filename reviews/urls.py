from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', TemplateView.as_view(template_name='reviews/review_home.html'), name='reviews-home'),
    path('courses/', TemplateView.as_view(template_name='reviews/course_reviews.html'), name='courses'),
    path('books/', TemplateView.as_view(template_name='reviews/book_reviews.html'), name='books'),
    path('software/', TemplateView.as_view(template_name='reviews/software_reviews.html'), name='software'),
    path('<int:review_id>/<slug:slug>/', views.review_detail, name='review-detail'),
]