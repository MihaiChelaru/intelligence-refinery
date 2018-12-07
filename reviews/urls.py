from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = 'reviews'

urlpatterns = [
    path('', TemplateView.as_view(template_name='reviews/review_home.html'), name='reviews-home'),
    path('<slug:resource_type>/', views.review_list, name='review-list'),
    path('<int:review_id>/<slug:slug>/', views.review_detail, name='review-detail'),
]