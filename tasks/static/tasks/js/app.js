// ========== Configuration ==========
const API_BASE_URL = '/api/tasks/';
let currentFilter = 'all';

// ========== Fonctions utilitaires ==========

/**
 * Afficher/masquer le loading
 */
function toggleLoading(show) {
    const loading = document.getElementById('loading');
    if (loading) {
        loading.classList.toggle('hidden', !show);
    }
}

/**
 * Afficher un message de succès
 */
function showSuccess(message) {
    const successMsg = document.getElementById('successMessage');
    successMsg.textContent = message;
    successMsg.classList.add('show');
    
    setTimeout(() => {
        successMsg.classList.remove('show');
    }, 3000);
}

/**
 * Formater la date
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('fr-FR', {
        day: '2-digit',
        month: '2-digit',
        year: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

/**
 * Obtenir l'icône de priorité
 */
function getPriorityIcon(priority) {
    const icons = {
        'high': '🔴',
        'medium': '🟡',
        'low': '🟢'
    };
    return icons[priority] || '⚪';
}

/**
 * Obtenir le texte de priorité
 */
function getPriorityText(priority) {
    const texts = {
        'high': 'Haute',
        'medium': 'Moyenne',
        'low': 'Basse'
    };
    return texts[priority] || priority;
}

/**
 * Échapper le HTML pour éviter XSS
 */
function escapeHtml(text) {
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
}

// ========== Chargement des statistiques ==========

async function loadStatistics() {
    try {
        const response = await fetch(`${API_BASE_URL}statistics/`);
        const data = await response.json();
        
        document.getElementById('totalTasks').textContent = data.total;
        document.getElementById('completedTasks').textContent = data.completed;
        document.getElementById('pendingTasks').textContent = data.pending;
        document.getElementById('completionRate').textContent = 
            data.completion_rate.toFixed(1) + '%';
        
    } catch (error) {
        console.error('Erreur lors du chargement des statistiques:', error);
    }
}

// ========== Chargement des tâches ==========

async function loadTasks() {
    toggleLoading(true);
    
    try {
        let url = API_BASE_URL;
        
        // Ajouter les filtres à l'URL
        if (currentFilter === 'completed') {
            url += '?completed=true';
        } else if (currentFilter === 'pending') {
            url += '?completed=false';
        } else if (currentFilter === 'high') {
            url += '?priority=high';
        }
        
        const response = await fetch(url);
        const tasks = await response.json();
        
        displayTasks(tasks);
        
    } catch (error) {
        console.error('Erreur lors du chargement des tâches:', error);
        showError('Impossible de charger les tâches');
    } finally {
        toggleLoading(false);
    }
}

/**
 * Afficher les tâches dans le DOM
 */
function displayTasks(tasks) {
    const tasksList = document.getElementById('tasksList');
    
    if (!tasks || tasks.length === 0) {
        tasksList.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">📭</div>
                <h3>Aucune tâche</h3>
                <p>Commencez par ajouter une tâche ci-dessus !</p>
            </div>
        `;
        return;
    }
    
    tasksList.innerHTML = '';
    
    tasks.forEach(task => {
        const taskCard = createTaskCard(task);
        tasksList.appendChild(taskCard);
    });
}

/**
 * Créer une carte de tâche
 */
function createTaskCard(task) {
    const card = document.createElement('div');
    card.className = `task-card ${task.completed ? 'completed' : ''} priority-${task.priority}`;
    card.innerHTML = `
        <div class="task-header">
            <span class="priority-badge priority-${task.priority}">
                ${getPriorityIcon(task.priority)} ${getPriorityText(task.priority)}
            </span>
            <span class="task-meta">${formatDate(task.created_at)}</span>
        </div>
        
        <h4 class="task-title">${escapeHtml(task.title)}</h4>
        
        ${task.description ? `<p class="task-description">${escapeHtml(task.description)}</p>` : ''}
        
        <div class="task-actions">
            <button onclick="toggleTask(${task.id}, ${task.completed})" 
                    class="btn btn-sm ${task.completed ? 'btn-warning' : 'btn-success'}">
                ${task.completed ? '↩️ Réactiver' : '✅ Compléter'}
            </button>
            <button onclick="deleteTask(${task.id})" 
                    class="btn btn-sm btn-danger">
                🗑️ Supprimer
            </button>
        </div>
    `;
    
    return card;
}

// ========== Ajouter une tâche ==========

document.getElementById('addTaskForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    
    const title = document.getElementById('taskTitle').value.trim();
    const description = document.getElementById('taskDescription').value.trim();
    const priority = document.getElementById('taskPriority').value;
    
    if (!title) {
        alert('Le titre est requis');
        return;
    }
    
    toggleLoading(true);
    
    try {
        const response = await fetch(API_BASE_URL, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: title,
                description: description,
                priority: priority,
                completed: false
            })
        });
        
        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(JSON.stringify(errorData));
        }
        
        // Réinitialiser le formulaire
        document.getElementById('taskTitle').value = '';
        document.getElementById('taskDescription').value = '';
        document.getElementById('taskPriority').value = 'medium';
        
        // Recharger les tâches et statistiques
        await loadTasks();
        await loadStatistics();
        
        showSuccess('Tâche ajoutée avec succès !');
        
    } catch (error) {
        console.error('Erreur lors de l\'ajout de la tâche:', error);
        alert('Erreur lors de l\'ajout de la tâche');
    } finally {
        toggleLoading(false);
    }
});

// ========== Basculer l'état d'une tâche ==========

async function toggleTask(taskId, currentStatus) {
    toggleLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}${taskId}/toggle/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            }
        });
        
        if (!response.ok) {
            throw new Error('Erreur lors de la mise à jour');
        }
        
        await loadTasks();
        await loadStatistics();
        
        showSuccess('Tâche mise à jour !');
        
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors de la mise à jour de la tâche');
    } finally {
        toggleLoading(false);
    }
}

// ========== Supprimer une tâche ==========

async function deleteTask(taskId) {
    if (!confirm('Êtes-vous sûr de vouloir supprimer cette tâche ?')) {
        return;
    }
    
    toggleLoading(true);
    
    try {
        const response = await fetch(`${API_BASE_URL}${taskId}/`, {
            method: 'DELETE'
        });
        
        if (!response.ok) {
            throw new Error('Erreur lors de la suppression');
        }
        
        await loadTasks();
        await loadStatistics();
        
        showSuccess('Tâche supprimée avec succès !');
        
    } catch (error) {
        console.error('Erreur:', error);
        alert('Erreur lors de la suppression de la tâche');
    } finally {
        toggleLoading(false);
    }
}

// ========== Filtrage ==========

function filterTasks(filter) {
    currentFilter = filter;
    
    // Mettre à jour les boutons actifs
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    document.getElementById(`filter-${filter}`).classList.add('active');
    
    // Recharger les tâches
    loadTasks();
}

// ========== Initialisation ==========

document.addEventListener('DOMContentLoaded', function() {
    // Charger les données initiales
    loadStatistics();
    loadTasks();
    
    // Rafraîchir les statistiques toutes les 30 secondes
    setInterval(loadStatistics, 30000);
});