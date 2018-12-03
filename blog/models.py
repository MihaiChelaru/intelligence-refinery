import tagulous.models
from django.db import models
from django.urls import reverse
from markdownx.models import MarkdownxField


# Site tags model
class SiteTags(tagulous.models.TagModel):

    @property
    def color(self):
        '''
        :return: Returns the hue value for this particular tag for use in CSS hsl() color property.
        '''
        hue = ((self.pk * 0.618033988749895) % 1) * 360
        return f'{hue}, 60%, 80%'

    def get_absolute_url(self):
        '''
        :return: Returns the URL to the posts-by-tag page corresponding to this particular tag.
        '''
        return reverse('posts-by-tag', kwargs={'slug': self.slug})

# Models for blog app
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(max_length=2000, help_text='Author biography')
    email = models.EmailField()
    github = models.URLField()
    stack_overflow = models.URLField(null=True, blank=True)

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
    tags = tagulous.models.TagField(to=SiteTags)

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk, 'slug': self.slug})

    def __str__(self):
        """
        Returns the title of the post.
        :return:
        """
        return self.title
