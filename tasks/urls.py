from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views, api_views

# Router DRF pour l'API
router = DefaultRouter()
router.register(r'tasks', api_views.TaskViewSet, basename='task')

urlpatterns = [
    # URLs traditionnelles (ce qu'on a déjà)
    path('', views.home, name='home'),
    path('ajax/', views.home_ajax, name='home_ajax'),
    path('toggle/<int:task_id>/', views.toggle_task, name='toggle_task'),
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    
    # URLs de l'API
    path('api/', include(router.urls)),
]