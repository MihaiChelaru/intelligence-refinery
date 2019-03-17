from blog.models import SiteTags
from dal import autocomplete
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=True, max_length=50)
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True, max_length=100)
    message = forms.CharField(widget=forms.Textarea, required=True)


class TagForm(forms.Form):
    tag = forms.ModelChoiceField(
        queryset=SiteTags.objects.all(),
        widget=autocomplete.ModelSelect2(url='tag-autocomplete')
    )
