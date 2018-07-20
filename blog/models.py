from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField


# Models for blog app
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000, help_text='Author biography')
    email = models.EmailField()

    def __str__(self):
        """
        String representation of the author of a post, "first_name last_name".
        :return:
        """
        return self.first_name + " " + self.last_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, help_text='Hyphen-separated string of keywords for SEO')
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    blurb = models.TextField(max_length=200, help_text='Short blurb summarizing article for list view')
    content = MarkdownxField()
    publication_date = models.DateField()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        """
        Returns the title of the post.
        :return:
        """
        return self.title
