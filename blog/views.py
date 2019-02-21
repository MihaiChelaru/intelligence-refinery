import markdown
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from markdownx.utils import markdownify

from .models import Post


# Views for blog app
def post_list(request):
    """
    View function for viewing a list of the 10 most recent posts.
    """
    posts = Post.objects.filter(publication_date__lte=timezone.now()).order_by('-publication_date')
    return render(request, 'blog/post_list.html', {"posts": posts})


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
    md = markdown.Markdown(extensions=[TocExtension(slugify=slugify),])
    html = md.convert(post.content)
    # markdownify() content and display on page
    post.content = markdownify(post.content)
    # Create table of contents to pass to context
    tab_oc = md.toc
    tab_oc = tab_oc.replace(r'div class="toc"', r'nav id="scrollSpy" class="navbar flex-column"')
    tab_oc = tab_oc.replace(r'</div>', r'</nav>')
    tab_oc = tab_oc.replace(r'<ul>', r'<nav class="nav nav-pills flex-column">')
    tab_oc = tab_oc.replace(r'</ul>', r'</nav>')
    tab_oc = tab_oc.replace(r'<li><a', r'<a class="nav-link"')
    tab_oc = tab_oc.replace(r'</li>', '')
    context = {
        'post': post,
        'author': author,
        'toc': tab_oc
    }
    return render(request, 'blog/post_detail.html', context)
