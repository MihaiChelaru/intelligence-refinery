from django.urls import path
from django.views.generic import TemplateView

app_name = 'reviews'

urlpatterns = [
    path('', TemplateView.as_view(template_name='reviews/course_reviews.html'), name='reviews'),
    path('<int:post_id>/<slug:slug>/', TemplateView.as_view(template_name='reviews/review_detail.html', name='review-detail'))
]