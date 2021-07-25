from django import forms
from .models import Category


class New_forms(forms.Form):
    title = forms.CharField(max_length=255, min_length=3)
    content = forms.CharField()
    is_published = forms.BooleanField
    category = forms.ModelChoiceField(queryset=Category.objects.all())
