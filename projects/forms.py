from django import forms
from django.utils import timezone

class ProjectForm(forms.Form):
    title = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea)
    technology = forms.ChoiceField(choices= (('1',"tech" ),('2',"games"),))
    collaborator = forms.CharField(max_length=100)