from django import forms
from .models import BlogEntries

class BlogForm(forms.ModelForm):

    class Meta:
        model = BlogEntries
        fields = ["name", "description", "tags"]