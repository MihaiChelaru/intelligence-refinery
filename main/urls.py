from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from blog.views import TagAutocomplete
from main import views

urlpatterns = [
    path('blog/', include('blog.urls')),
    path('reviews/', include('reviews.urls')),
    path('admin/', admin.site.urls, {}),
    path('', views.home, name='home'),
    path('markdownx/', include('markdownx.urls')),
    path('contact/', views.contact, name='contact'),
    path('success/', TemplateView.as_view(template_name='main/success.html'), name='success'),
    path('portfolio/', TemplateView.as_view(template_name='main/portfolio.html'), name='portfolio'),
    path('resources/', TemplateView.as_view(template_name='main/resources.html'), name='resources'),
    path('portfolio/curriculum-vitae/', views.curriculum_vitae_view, name='curriculum-vitae'),
    path('portfolio/cannabis-eda/', TemplateView.as_view(template_name='main/cannabis_strains_EDA.html'), name='cannabis-eda'),
    path('portfolio/telco-churn/', TemplateView.as_view(template_name='main/telco_churn.html'), name='telco-churn'),
    path('tags/', views.tag_list, name='tag-list'),
    path('tags/<slug:slug>/', views.posts_by_tag, name='posts-by-tag'),
    path('tag-autocomplete/', TagAutocomplete.as_view(), name='tag-autocomplete'),
    path('tag-search/', views.tag_search, name='tag-search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns