from django.shortcuts import render
from django.views import View
from ..models.skills import Skill

class SkillsPageView(View):
    def get(self, request):
        skills = Skill.objects.order_by('-id')
        return render(request, 'skills.html', {"skills": skills})
