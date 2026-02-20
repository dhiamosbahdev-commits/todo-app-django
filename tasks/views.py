from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def home(request):
    """
    Vue principale : affiche et gère les tâches
    """
    # Ajouter une nouvelle tâche (POST)
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description', '')
        priority = request.POST.get('priority', 'medium')
        
        if title:
            Task.objects.create(
                title=title,
                description=description,
                priority=priority
            )
            return redirect('home')
    
    # Filtrer les tâches (GET)
    filter_by = request.GET.get('filter', 'all')
    
    if filter_by == 'completed':
        tasks = Task.objects.filter(completed=True)
    elif filter_by == 'pending':
        tasks = Task.objects.filter(completed=False)
    else:
        tasks = Task.objects.all()
    
    context = {
        'tasks': tasks,
        'current_filter': filter_by
    }
    
    return render(request, 'tasks/home.html', context)


def toggle_task(request, task_id):
    """
    Basculer l'état d'une tâche (complétée/non complétée)
    """
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('home')


def delete_task(request, task_id):
    """
    Supprimer une tâche
    """
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('home')
# Create your views here.
def home_ajax(request):
    """
    Page d'accueil AJAX
    """
    return render(request, 'tasks/home_ajax.html')