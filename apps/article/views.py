from django.shortcuts import render, get_object_or_404
from django.views import View

from .models.article import Article

class BlogPageView(View):
    def get(self, request):
        articles = Article.objects.select_related('category', 'author').order_by('-created_at')
        return render(request, 'articles.html', {'articles': articles})

class BlogDetailPageView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article.objects.select_related('category', 'author'), slug=slug)
        article.views += 1
        article.save(update_fields=['views'])
        return render(request, 'article-detail.html', {'article': article})
