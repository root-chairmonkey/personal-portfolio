
from django.db.models.query import QuerySet
from django.forms.forms import Form
from django.shortcuts import render , redirect
from projects.forms import ProjectForm
from projects.models import Project
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='base_index')
def project_index(request):
    projects = Project.objects.all()
    form = ProjectForm()
    activeProjects = Project.objects.filter(status='active')
    totalNumactiveProjects = len(activeProjects)
    totalNumProjects = len(projects)
    #count = 0
    #allCollaboratorList = []
    #while count < totalNumactiveProjects:
        #allCollaboratorList.append(projects[count].collaborator)
        #count = count+1

    context = {
        'projects': projects,
        'form': form,
        'totalNumProjects': totalNumProjects,
        'activeProjects': activeProjects,
        'totalNumactiveProjects': totalNumactiveProjects,
        #'allCollaboratorList': allCollaboratorList,
    }
    return render(request, 'project_index.html', context)

#@login_required(login_url='base_index')
def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    
    return render(request, 'project_detail.html', context)

def project_create(request):
    if request.method == "POST":
        form = ProjectForm(request.POST)
        title = request.POST['title']
        description = request.POST['description']
        technology = request.POST['technology']
        collaborator = request.POST['collaborator']
        status = request.POST['status']
        project = Project.objects.create(title=title, description=description, 
                    technology=technology, collaborator=collaborator, status=status)
        project.save()

    return JsonResponse({'status':'submitted'})
    