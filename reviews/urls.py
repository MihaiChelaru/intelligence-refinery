from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'reviews'

#TODO: add reviews-by-tag view similar to blog equivalent
urlpatterns = [
    path('', TemplateView.as_view(template_name='reviews/course_reviews.html'), name='reviews'),
    path('<int:review_id>/<slug:slug>/', views.review_detail, name='review-detail')
]