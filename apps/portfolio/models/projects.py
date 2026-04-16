from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Project(models.Model):
    name = models.CharField(max_length=150, unique=True, db_index=True)
    slug = models.SlugField(max_length=225, unique=True, null=True, blank=True, db_index=True)
    technologies = models.ManyToManyField('portfolio.Technology', related_name='projects', blank=True)
    description = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True, unique=True, max_length=225, db_index=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['slug']),
            models.Index(fields=['link']),
        ]

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('project-detail', kwargs={'slug': self.slug})
