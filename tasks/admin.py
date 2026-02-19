#from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'completed', 'created_at', 'due_date']
    list_filter = ['completed', 'priority', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['completed', 'priority']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('title', 'description')
        }),
        ('État et priorité', {
            'fields': ('completed', 'priority')
        }),
        ('Dates', {
            'fields': ('due_date',),
        }),
    )