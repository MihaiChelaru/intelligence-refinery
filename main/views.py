from blog.models import SiteTags, Post
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, FileResponse, Http404
from django.shortcuts import render, redirect
from django.templatetags.static import static
from reviews.models import Review

from .forms import ContactForm


def home(request):
    """
    View Function for home page of the site.
    :param request:
    :return:
    """
    return render(
        request, 'main/home.html', context={}
    )

def contact(request):
    """
    View for displaying the contact form page.
    :param request:
    :return:
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message =  f"Sent by: {name} <{email}>\n\n" + form.cleaned_data['message']
            try:
                send_mail(subject, message, "mailgun@mg.intelligencerefinery.io", ['admin@intelligencerefinery.io'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form':form})


def tag_list(request):
    """
    View function for viewing a list of links to all tags from all posts.
    :param request:
    :param slug: Tag slug.
    :return:
    """
    tags = SiteTags.objects.all()
    return render(request, 'main/tag_list.html', {'tags': tags})

def posts_by_tag(request, slug):
    """
    View for displaying all posts with a given tag.
    :param request:
    :param slug:
    :return:
    """
    blog_posts = Post.objects.filter(tags=slug)
    reviews = Review.objects.filter(tags=slug)
    return render(request, 'main/posts_by_tag.html', {'blog_posts': blog_posts, 'reviews': reviews,'slug':slug})

def curriculum_vitae_view(request):
    try:
        return FileResponse(open(static('pdf/Mihai_Chelaru_CV.pdf'), 'rb'))
    except FileNotFoundError:
        raise Http404("Could not find PDF.")
