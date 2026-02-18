# 📝 Application de gestion des tâches

> Application web développée avec Django et Django REST Framework

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Django](https://img.shields.io/badge/Django-4.2+-green.svg)
![DRF](https://img.shields.io/badge/DRF-3.14+-red.svg)

## 🚀 Statut du projet

**En cours de développement** - Formation CYBERPARC GR01

- **Début :** 17 février 2026
- **Livraison prévue :** 2 mars 2026
- **Développeur :** Dhia Mosbah

## 📋 Fonctionnalités prévues

- ✅ Gestion CRUD complète des tâches
- ✅ Système de priorités (haute, moyenne, basse)
- ✅ API REST avec Django REST Framework
- ✅ Interface AJAX interactive
- ✅ Filtrage et statistiques en temps réel
- ✅ Design responsive

## 🛠️ Technologies

- **Backend :** Python 3.8+, Django 4.2
- **API :** Django REST Framework 3.14
- **Frontend :** HTML5, CSS3, JavaScript ES6+
- **Base de données :** SQLite (dev)

## 📦 Installation
```bash
# Cloner le repository
git clone https://github.com/dhiamosbahdev/todo-app-django.git
cd todo-app-django

# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Windows PowerShell:
venv\Scripts\Activate.ps1
# Windows CMD:
venv\Scripts\activate.bat
# Mac/Linux:
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt

# Appliquer les migrations
python manage.py migrate

# Créer un superuser
python manage.py createsuperuser

# Lancer le serveur
python manage.py runserver
```

## 📚 Documentation

Documentation complète à venir lors de la livraison finale.

---

**Développé par Dhia Mosbah** - CYBERPARC GR01  
*Formation Django & DRF - Février 2026*
```

3. **Sauvegarder** : `Ctrl+S`

#### **Étape 9 : Créer LICENSE**

1. **New File** → `LICENSE`
2. **Copier :**
```
MIT License

Copyright (c) 2026 Dhia Mosbah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

#### **Étape 10 : Premier commit avec l'interface VS Code**

**Méthode graphique (facile) :**

1. **Cliquer sur l'icône Git** (3ème icône à gauche, branches)
2. **Voir** tous les fichiers non trackés :
   - `.gitignore`
   - `README.md`
   - `LICENSE`
   - `requirements.txt`
3. **Survoler "Changes"** → **Cliquer sur le "+"** (Stage All Changes)
4. **Taper un message** dans la zone en haut :
```
   Initial commit: Project structure and documentation
```
5. **Cliquer sur le ✓** (Commit) ou `Ctrl+Enter`

**✅ Commit créé !**

---

## **PHASE 3 : LIER À GITHUB**

### **Étape 1 : Créer le repository sur GitHub**

**Ouvrir le navigateur :**

1. **Aller sur** : https://github.com/dhiamosbahdev
2. **Se connecter** (si pas déjà fait)
3. **Cliquer** : **"New"** (bouton vert en haut à droite)
4. **Remplir :**
```
   Repository name: todo-app-django
   Description: Application de gestion des tâches - Django & DRF
   
   ☑ Public
   
   ❌ Add a README file (on l'a déjà)
   ❌ Add .gitignore (on l'a déjà)
   ❌ Choose a license (on l'a déjà)