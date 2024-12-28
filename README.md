# Wawel Patisseries

Bienvenue sur le site web officiel de **Wawel**, une pâtisserie artisanale spécialisée dans les créations gourmandes d'exception.

## Description du projet

Ce projet est un site web conçu pour mettre en avant les produits et services de la pâtisserie Wawel. Il permet de :

- Présenter les informations sur la pâtisserie et son histoire.
- Afficher les produits disponibles sous forme de menu.
- Fournir un formulaire de contact pour les clients.
- Informer les visiteurs sur la politique de confidentialité.

## Fonctionnalités principales

1. **Page d'accueil :**
   - Présentation des promotions actuelles.
   - Introduction à la pâtisserie et ses engagements.

2. **Page À propos :**
   - Histoire et valeurs de la pâtisserie.

3. **Page Produits :**
   - Menu organisé par catégories et sous-catégories.
   - Possibilité d'ajouter de nouvelles catégories et produits via l'administration.

4. **Page Contact :**
   - Formulaire de contact dynamique.
   - Envoi d'e-mails directement depuis le formulaire.

5. **Page Politique de confidentialité :**
   - Informations détaillées sur la gestion des données personnelles des utilisateurs.

6. **Administration :**
   - Gestion des produits, promotions et abonnés à la newsletter.
   - Personnalisation des contenus via le panneau d'administration de Django.

## Technologies utilisées

- **Django (Framework backend)** : Gestion des modèles, des vues et des templates.
- **HTML5, CSS3, JavaScript** : Création d'une interface utilisateur moderne et interactive.
- **SQLite3** : Base de données légère pour stocker les données.
- **Django Email Backend** : Gestion sécurisée de l'envoi d'e-mails.

## Prérequis

- Python 3.x
- Pipenv ou virtualenv pour la gestion des environnements virtuels.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone <lien_du_dépôt>
   cd Wawel-main
   ```

2. Créez et activez un environnement virtuel :

   ```bash
   python -m venv env
   source env/bin/activate # sous Windows : env\Scripts\activate
   ```

3. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

4. Configurez les variables d'environnement dans un fichier `.env` :

   ```env
   SECRET_KEY='votre_clé_secrète_django'
   DEBUG=True
   EMAIL_HOST_USER='votre_email@gmail.com'
   EMAIL_HOST_PASSWORD='votre_mot_de_passe'
   ```

5. Appliquez les migrations de la base de données :

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Lancez le serveur de développement :

   ```bash
   python manage.py runserver
   ```

7. Accédez au site à l'adresse : [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Structure du projet

- **templates/** : Contient tous les fichiers HTML pour le rendu des pages.
- **static/** : Contient les fichiers CSS, JavaScript et les images.
- **models.py** : Définit les modèles pour les produits, clients, promotions, etc.
- **views.py** : Gère la logique des pages et des interactions utilisateur.
- **forms.py** : Définit les formulaires pour les produits et promotions.
- **urls.py** : Gère les routes du site.

## Fonctionnalités à venir

- Intégration d'un système de commande en ligne.
- Ajout d'une page "Blog" pour partager des recettes et des conseils pâtissiers.
- Notifications par e-mail pour les promotions spéciales.

## Auteurs

- **Ines Oubabas** - Développement backend et intégration frontend.
- **Équipe Wawel** - Contributions diverses.

## Licence

Ce projet est sous licence MIT. Consultez le fichier LICENSE pour plus d'informations.

---

Merci de visiter notre site et de soutenir la pâtisserie Wawel. Nous espérons que vous apprécierez nos créations gourmandes !
