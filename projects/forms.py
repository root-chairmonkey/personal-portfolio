from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from django.utils import timezone
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'collaborator']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'id': 'titleid'}),
            'description': forms.TextInput(attrs={'class': 'form-control', 'id': 'descriptionid'}),
            'technology' : forms.TextInput(attrs={'class': 'form-control', 'id': 'technologyid'}),
            'collaborator': forms.TextInput(attrs={'class': 'form-control', 'id': 'collaboratorid'}),                                  
        }
    #title = forms.CharField(max_length=100)
    #description = forms.CharField(widget=forms.Textarea)
    #technology = forms.ChoiceField(choices=(("tech", "tech"),))
    #collaborator = forms.CharField(max_length=100)