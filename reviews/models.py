from django.db import models
from django.urls import reverse
from intelligencerefinery.blog.models import Author, Tags
from markdownx.models import MarkdownxField
from tagulous.models import TagField


class Resource(models.Model):
    """
    Type of resource, such as a course or data repository.
    """
    name = models.CharField(max_length=100)


class Review(models.Model):
    resource_name = models.CharField(max_length=100)
    url = models.URLField(null=True, blank=True)
    github_url = models.URLField(null=True, blank=True)
    slug = models.SlugField(max_length=40, help_text='Hyphen-separated string of keywords for SEO')
    review_author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    resource_author = models.CharField(max_length=100, null=True, blank=True)
    blurb = models.TextField(max_length=200, help_text='Short blurb summarizing review for list view')
    content = MarkdownxField()
    last_updated = models.DateField()
    tags = TagField(to=Tags)
    resource_type = models.ForeignKey(Resource, on_delete=models.SET_NULL, null=True)

    def get_absolute_url(self):
        return reverse('review-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        """
        Returns the title of the review.
        :return:
        """
        return self.resource_name
