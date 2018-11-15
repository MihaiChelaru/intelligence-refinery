from django.urls import path
from django.views.generic import TemplateView

app_name = 'reviews'

urlpatterns = [
    path('', TemplateView.as_view(template_name='reviews/course_reviews.html'), name='reviews')
]