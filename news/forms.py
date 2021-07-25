from django import forms
from .models import Category


class New_forms(forms.Form):
    title = forms.CharField(max_length=255, min_length=3, label='Title',
                            widget=forms.TextInput(attrs={'class': "form-control"}))
    content = forms.CharField(label='Content:', required=False,
                              widget=forms.Textarea(attrs={'class': "form-control"}))
    is_published = forms.BooleanField(label='Published?', initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label='Category:',
                                      empty_label='Please choose category',
                                      widget=forms.Select(attrs={'class': "form-control"}))
