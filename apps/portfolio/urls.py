from django.urls import path

from .views.home import HomePageView
from .views.about import AboutPageView
from .views.projects import ProjectPageView, ProjectDetailPageView
from .views.resume import ResumePageView
from .views.skills import SkillsPageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('projects/', ProjectPageView.as_view(), name='projects'),
    path('project-detail/<slug:slug>/', ProjectDetailPageView.as_view(), name='project-detail'),
    path('resume/', ResumePageView.as_view(), name='resume'),
    path('skills/', SkillsPageView.as_view(), name='skills')
]
