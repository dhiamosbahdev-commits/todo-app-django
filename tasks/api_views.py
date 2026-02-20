from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Task
from .serializers import TaskSerializer

class TaskViewSet(viewsets.ModelViewSet):
    """
    ViewSet pour l'API des tâches
    Fournit automatiquement les actions CRUD
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        """
        Permet de filtrer les tâches via les paramètres URL
        Exemples:
        - /api/tasks/?completed=true
        - /api/tasks/?priority=high
        - /api/tasks/?search=django
        """
        queryset = super().get_queryset()
        
        # Filtrer par statut de complétion
        completed = self.request.query_params.get('completed')
        if completed is not None:
            is_completed = completed.lower() == 'true'
            queryset = queryset.filter(completed=is_completed)
        
        # Filtrer par priorité
        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority=priority)
        
        # Recherche dans titre et description
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) | 
                Q(description__icontains=search)
            )
        
        return queryset
    
    @action(detail=False, methods=['get'])
    def statistics(self, request):
        """
        Endpoint personnalisé pour les statistiques
        GET /api/tasks/statistics/
        """
        total = Task.objects.count()
        completed = Task.objects.filter(completed=True).count()
        pending = Task.objects.filter(completed=False).count()
        
        # Statistiques par priorité
        priority_stats = {
            'high': Task.objects.filter(priority='high').count(),
            'medium': Task.objects.filter(priority='medium').count(),
            'low': Task.objects.filter(priority='low').count(),
        }
        
        # Taux d'achèvement
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        return Response({
            'total': total,
            'completed': completed,
            'pending': pending,
            'completion_rate': round(completion_rate, 2),
            'priority_distribution': priority_stats
        })
    
    @action(detail=True, methods=['post'])
    def toggle(self, request, pk=None):
        """
        Endpoint pour basculer le statut completed
        POST /api/tasks/5/toggle/
        """
        task = self.get_object()
        task.completed = not task.completed
        task.save()
        
        serializer = self.get_serializer(task)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def recent(self, request):
        """
        Retourne les 10 tâches les plus récentes
        GET /api/tasks/recent/
        """
        recent_tasks = Task.objects.all()[:10]
        serializer = self.get_serializer(recent_tasks, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def overdue(self, request):
        """
        Retourne les tâches en retard
        GET /api/tasks/overdue/
        """
        from django.utils import timezone
        overdue_tasks = Task.objects.filter(
            due_date__lt=timezone.now(),
            completed=False
        )
        serializer = self.get_serializer(overdue_tasks, many=True)
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        """
        Surcharger la méthode destroy pour retourner un message
        """
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {'message': 'Tâche supprimée avec succès'},
            status=status.HTTP_200_OK
        )