
from django.forms.forms import Form
from django.shortcuts import render , redirect
from projects.forms import ProjectForm
from projects.models import Project
from django.urls import reverse_lazy

# Create your views here.

def project_index(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    
    return render(request, 'project_detail.html', context)

def project_create(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        technology = request.POST['technology']
        collaborator = request.POST['collaborator']
        
        project = Project.objects.create(title=title, description=description, 
                    technology=technology, collaborator=collaborator)
        project.save()

        projects = Project.objects.all()
        context = {
            'projects': projects
        }
        return render(request,'project_index.html', context)

    else:
        form = ProjectForm()
        context = {
            'form' : form
            }
        return render(request, 'project_create.html', context)
    
    