from django.db import models

class Technology(models.Model):    
    name = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Technology'
        verbose_name_plural = 'Technologies'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name}"
