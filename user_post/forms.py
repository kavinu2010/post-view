from django import forms
from .models import Poster

class PostForm(forms.ModelForm):
  class Meta:
    model=Poster
    fields=['title','comment','written_by']
