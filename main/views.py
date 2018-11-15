from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.shortcuts import render, redirect

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