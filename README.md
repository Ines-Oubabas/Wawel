# **WAWEL - Site Web pour la Boulangerie et Pâtisserie**

## 📋 **Description du projet**

**WAWEL** est un site web conçu pour faciliter la communication entre une boulangerie-pâtisserie et ses clients. Le site permet :
- D'afficher les produits proposés (pains, viennoiseries, salés, etc.).
- De permettre aux clients d'envoyer des messages via un formulaire de contact.
- De présenter l'histoire et l'équipe de la boulangerie dans la page **À propos**.
- De gérer des produits, clients et promotions grâce à une interface d'administration dédiée.

Ce projet a été développé avec le framework **Django** et suit une structure MVC (Model-View-Controller).

---

## 🚀 **Fonctionnalités principales**

1. **Page d'accueil** :
   - Accueil chaleureux avec présentation du site.

2. **Page Produits** :
   - Catégories et sous-catégories organisées avec des images, descriptions et codes des produits.

3. **Page Contact** :
   - Les clients peuvent envoyer des messages directement via un formulaire sécurisé.
   - Confirmation de l'envoi avec une page **"Message envoyé avec succès"**.

4. **Page À propos** :
   - Présentation de l'histoire, des valeurs et de l'équipe de la boulangerie.

5. **Administration** :
   - Gestion des produits, clients et promotions.
   - Ajout de nouveaux produits avec images et descriptions.

---

## 🛠️ **Technologies utilisées**

- **Backend** : Django (Python)
- **Frontend** : HTML5, CSS3, JavaScript
- **Base de données** : SQLite
- **Envoi d'email** : SMTP avec Gmail
- **Hébergement** : Serveur local (pour le développement)

---

## 📂 **Structure du projet**

```
WAWEL/
👉 magasin/                     # Application principale Django
👉       migrations/              # Fichiers de migration de la base de données
👉       static/                  # Fichiers statiques (CSS, images)
👉       templates/               # Fichiers HTML
👉       ┗️ utils/               # Composants réutilisables (ex: nav.html)
👉       ┗️ index.html           # Page d'accueil
👉       ┗️ produits.html        # Page des produits
👉       ┗️ contact.html         # Page de contact
👉       ┗️ about.html           # Page à propos
👉       ┗️ success.html         # Page de confirmation de message
👉       ┗️ admin/               # Pages d'administration
👉       forms.py                 # Formulaires Django
👉       models.py                # Modèles de données (Produits, Clients, Promotions)
👉       views.py                 # Logique métier (vues Django)
👉       urls.py                  # Configuration des routes URL

👉 wawel/                       # Configuration du projet Django
👉 db.sqlite3                   # Base de données SQLite
👉 manage.py                    # Commande pour gérer le projet Django
👉 README.md                    # Documentation du projet
```

---

## 📦 **Installation du projet**

### **1. Cloner le projet**
```bash
git clone https://github.com/nom-utilisateur/wawel.git
cd wawel
```

### **2. Configurer l'environnement virtuel**
```bash
python -m venv env
source env/bin/activate       # Sur macOS/Linux
env\Scripts\activate          # Sur Windows
```

### **3. Installer les dépendances**
```bash
pip install -r requirements.txt
```

### **4. Configurer l'email SMTP (settings.py)**
Remplacez les paramètres suivants dans **wawel/settings.py** avec vos informations Gmail :

```python
EMAIL_HOST_USER = 'votre-adresse-email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre-mot-de-passe-d-application'
```

### **5. Appliquer les migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **6. Lancer le serveur local**
```bash
python manage.py runserver
```

Accédez au site à l'adresse **http://127.0.0.1:8000/**.

---

## 📈 **Pages principales**
- **Accueil** : Page d'accueil générale.
- **Produits** : Catégories et produits proposés.
- **Contact** : Formulaire pour envoyer un message.
- **À propos** : Informations sur l'entreprise.
- **Administration** : Pages pour gérer les produits et les clients.

---

## 👥 **Crédits**
- **Développement** : Ines Oubabas
- **Icônes utilisées** : [Tick icons created by Octopocto - Flaticon](https://www.flaticon.com/free-icons/tick)
- **Framework** : Django

---

## 📝 **Licence**
Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le partager.

---
