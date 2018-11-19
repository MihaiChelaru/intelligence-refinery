from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Review, Resource

admin.site.register(Resource)

@admin.register(Review)
class ReviewAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {"slug": ("resource_name",)}