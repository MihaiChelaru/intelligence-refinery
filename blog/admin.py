from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from .models import Post, Author

# Register blog models for the admin site here.
admin.site.register(Author)


@admin.register(Post)
class PostAdmin(MarkdownxModelAdmin):
    prepopulated_fields = {"slug": ("title",)}