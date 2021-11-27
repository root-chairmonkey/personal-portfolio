from django import forms
from django.db.models.base import Model
from django.forms import fields, widgets
from django.utils import timezone
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'technology', 'collaborator', 'status']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control-sm', 'id': 'titleid', 'size':'40'}),
            'description': forms.TextInput(attrs={'class': 'form-control-lg', 'id': 'descriptionid','size':'40'}),
            'technology' : forms.TextInput(attrs={'class': 'form-control-sm', 'id': 'technologyid', 'size':'40'}),
            'collaborator': forms.TextInput(attrs={'class': 'form-control-sm', 'id': 'collaboratorid', 'size':'40'}), 
            'status': forms.TextInput(attrs={'class': 'form-control-sm', 'id': 'statusid', 'size':'40'}),                                 
        }
    #title = forms.CharField(max_length=100)
    #description = forms.CharField(widget=forms.Textarea)
    #technology = forms.ChoiceField(choices=(("tech", "tech"),))
    #collaborator = forms.CharField(max_length=100)