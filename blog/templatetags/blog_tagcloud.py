from blog import models
from django import template

register = template.Library()

@register.inclusion_tag('blog/tagcloud.html')
def tag_cloud():
    tags = models.Tags.weight()
    return {'tags': tags}
