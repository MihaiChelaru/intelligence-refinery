"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

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
    # wiki urls
    path('notifications/', include('django_nyt.urls')),
    path('wiki/', include('wiki.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns