from django import forms
from django.urls import reverse


class SourceForm(forms.Form):
    source_link = forms.URLField()

    def get_absolute_url(self):
        return reverse("homepage")

