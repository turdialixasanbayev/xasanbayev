from django.db import models

class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True, db_index=True)

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['-id']
        indexes = [
            models.Index(fields=['name']),
        ]

    def __str__(self):
        return f"{self.name}"
