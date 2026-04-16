from django.urls import path
from .views import (
    BlogDetailPageView,
    BlogPageView
)

urlpatterns = [
    path('articles/', BlogPageView.as_view(), name='articles'),
    path('article-detail/<slug:slug>/', BlogDetailPageView.as_view(), name='article-detail')
]
