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
    # request = context['request']
    # if request.method == 'POST':
    #     form = TagForm(request.POST)
    #     if form.is_valid():
    #         slug = form.cleaned_data['tag']
    #         return redirect('posts-by-tag', slug=slug)
    form = TagForm()
    return {'form': form}

@register.filter()
def to_int(value):
    return int(value)
