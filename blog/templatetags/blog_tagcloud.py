from blog import models
from django import template
from main.forms import TagForm

register = template.Library()

@register.inclusion_tag('blog/tagcloud.html')
def tag_cloud():
    tags = models.SiteTags.objects.weight()
    return {'tags': tags}

# TODO: include this form into the tag_autocomplete.html template, then include the tag in the site navbar
@register.inclusion_tag('blog/tag_autocomplete.html')
def tag_autocomplete():
    form = TagForm()
    return {'form': form}

@register.filter()
def to_int(value):
    return int(value)