from blog import models
from django import template

register = template.Library()

@register.inclusion_tag('blog/tagcloud.html')
def tag_cloud():
    tags = models.SiteTags.objects.weight()
    return {'tags': tags}

@register.filter()
def to_int(value):
    return int(value)