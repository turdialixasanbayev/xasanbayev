from django.db import models

class ContactUS(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField(max_length=100, db_index=True)
    phone = models.CharField(max_length=20, null=True, blank=True, db_index=True)
    subject = models.CharField(max_length=100, null=True, blank=True)
    message = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contact US"
        verbose_name_plural = "Contact US"
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['email']),
            models.Index(fields=['phone']),
        ]

    def __str__(self):
        return f"{self.name} - {self.email}"
