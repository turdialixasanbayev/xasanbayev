from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Article(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, null=True, blank=True, db_index=True)
    category = models.ForeignKey('article.Category', on_delete=models.CASCADE, related_name='articles')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='article')
    image = models.ImageField(upload_to="article/images/", null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
        ]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return f"{self.name}"
