from django.shortcuts import render
from django.utils import timezone
from markdownx.utils import markdownify

from .models import Post


# Views for blog app

def post_list(request):
    """
    View function for viewing a list of the 10 most recent posts.
    """
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:10]
    for post in posts:
        post.content = markdownify(post.content)
    return render(request, 'blog/index.html', {'latest_posts': posts})