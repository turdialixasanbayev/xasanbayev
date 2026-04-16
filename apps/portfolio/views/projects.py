from django.shortcuts import render, get_object_or_404
from django.views import View
from ..models.projects import Project

class ProjectPageView(View):
    def get(self, request):
        projects = Project.objects.prefetch_related('technologies').order_by('-id')
        return render(request, 'projects.html', {'projects': projects})

class ProjectDetailPageView(View):
    def get(self, request, slug):
        project = get_object_or_404(Project.objects.prefetch_related('technologies'), slug=slug)
        return render(request, 'project-detail.html', {'project': project})
