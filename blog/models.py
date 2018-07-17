from django.db import models
from markdownx.models import MarkdownxField


# Models for blog app
class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000, help_text='Author biography')
    email = models.EmailField()


class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    content = MarkdownxField()
    publication_date = models.DateField()




