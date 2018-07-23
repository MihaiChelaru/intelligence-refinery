from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from markdownx.utils import markdownify

from .models import Post


# Views for blog app
def post_list(request):
    """
    View function for viewing a list of the 10 most recent posts.
    """
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')[:10]
    return render(request, 'blog/index.html', {"latest_posts": posts})


def post_detail(request, post_id, slug):
    """
    View function for viewing an individual blog post. Redirects to the correct slug if it is improperly entered.
    :param request:
    :param post_id:
    :param slug:
    :return:
    """
    # Checks if the slug in the URL matches the database, and if not redirects to the correct slug URL
    post = get_object_or_404(Post, pk=post_id)
    if post.slug != slug:
        return redirect('blog:post-detail', post_id=post.pk, slug=post.slug)
    author = post.author
    # markdownify() content and display on page
    post.content = markdownify(post.content)
    return render(request, 'blog/post_detail.html', {'post': post, 'author': author})

def tag_list(request):
    """
    View function for viewing a list of links to all tags from all posts.
    :param request:
    :param slug: Tag slug.
    :return:
    """
    tags = Post.tags.tag_model.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def posts_by_tag(request, slug):
    """
    View for displaying all posts with a given tag.
    :param request:
    :param slug:
    :return:
    """
    posts = Post.objects.filter(tags__slug__exact=slug)
    return render(request, 'blog/posts_by_tag.html', {'posts': posts, 'slug':slug})