from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer pour le modèle Task
    Convertit les objets Task en JSON et vice-versa
    """
    # Champ en lecture seule (calculé automatiquement)
    is_overdue = serializers.ReadOnlyField()
    
    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'completed',
            'priority',
            'created_at',
            'updated_at',
            'due_date',
            'is_overdue'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_title(self, value):
        """
        Validation personnalisée du titre
        """
        if len(value) < 3:
            raise serializers.ValidationError(
                "Le titre doit contenir au moins 3 caractères."
            )
        return value
    
    def validate(self, data):
        """
        Validation globale
        """
        # Vérifier que la date limite n'est pas dans le passé
        if data.get('due_date'):
            from django.utils import timezone
            if data['due_date'] < timezone.now():
                raise serializers.ValidationError({
                    'due_date': "La date limite ne peut pas être dans le passé."
                })
        return data