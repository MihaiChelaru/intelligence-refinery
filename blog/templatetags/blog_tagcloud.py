from blog import models
from django import template

register = template.Library()

@register.inclusion_tag('blog/tagcloud.html')
def tag_cloud():
    tags = models.Post.tags.tag_model.objects.weight()
    return {'tags': tags}
