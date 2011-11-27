from django.views.generic import list_detail
from django.shortcuts import get_object_or_404
from project.models import Project

def project_detail(request, project_id):
    # Look up the Author (and raise a 404 if she's not found)
    project = get_object_or_404(Project, pk=project_id)
    print 'project_detail', project
    # Show the detail page
    return list_detail.object_detail(
        request,
        queryset = Project.objects.all(),
        object_id = project_id,
        extra_context = {"p" : project}
    )