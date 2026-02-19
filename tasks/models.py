#from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Task(models.Model):
    """
    Modèle pour gérer les tâches
    """
    PRIORITY_CHOICES = [
        ('low', 'Basse'),
        ('medium', 'Moyenne'),
        ('high', 'Haute'),
    ]
    
    title = models.CharField(
        max_length=200,
        verbose_name="Titre"
    )
    description = models.TextField(
        blank=True,
        verbose_name="Description"
    )
    completed = models.BooleanField(
        default=False,
        verbose_name="Complétée"
    )
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='medium',
        verbose_name="Priorité"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Date de création"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Date de modification"
    )
    due_date = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="Date limite"
    )
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Tâche"
        verbose_name_plural = "Tâches"
    
    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        """Vérifie si la tâche est en retard"""
        if self.due_date and not self.completed:
            return timezone.now() > self.due_date
        return False