from django.utils import timezone
from django.views import generic

from .models import Post


# Views for blog app
class IndexView(generic.ListView):
    """
    View function for the main page of the blog app.
    """
    template_name = 'blog/index.html'
    context_object_name = 'latest_post_list'

    def get_queryset(self):
        """Return the last ten published posts (not including those set
        to be published in the future)."""
        return Post.objects.filter(
            publication_date__lte=timezone.now()
        ).order_by('-publication_date')[:10]