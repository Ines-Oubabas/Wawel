Voici une version améliorée de votre fichier README avec les modifications demandées :  

```markdown
# Wawel Pâtisseries et Boulangerie

Bienvenue sur le site web officiel de **Wawel**, une pâtisserie et boulangerie artisanale spécialisée dans les créations gourmandes et le savoir-faire traditionnel.

---

## 🥐 Description du projet

Ce projet est un site web conçu pour mettre en avant les produits et services de la pâtisserie et boulangerie **Wawel**. Il permet de :
- Présenter les informations sur l'histoire et les valeurs de la boutique.
- Afficher les produits sous forme de menu organisé par catégories et sous-catégories.
- Proposer un formulaire de contact interactif.
- Informer les visiteurs sur la politique de confidentialité et la gestion des données personnelles.

---

## 🌟 Fonctionnalités principales

1. **Page d'accueil :**
   - Présentation des promotions actuelles.
   - Introduction à l'univers de la pâtisserie et boulangerie Wawel.

2. **Page À propos :**
   - Histoire, engagement, et valeurs de la boutique.

3. **Page Produits :**
   - Menu organisé par catégories et sous-catégories.
   - Gestion facile des produits et catégories via l'administration.

4. **Page Contact :**
   - Formulaire dynamique pour contacter la boutique.
   - Envoi direct des messages par e-mail.

5. **Page Politique de confidentialité :**
   - Informations claires sur la gestion des données des utilisateurs.

6. **Administration :**
   - Gestion des produits, promotions, et abonnés à la newsletter via le panneau Django.
   - Personnalisation des contenus du site.

---

## ⚙️ Technologies utilisées

- **Django (Backend)** : Gestion des modèles, vues, templates, et logique applicative.
- **HTML5, CSS3, JavaScript** : Création d'une interface utilisateur moderne et interactive.
- **SQLite3** : Base de données pour stocker les informations.
- **Django Email Backend** : Gestion sécurisée de l'envoi d'e-mails.
- **Responsive Design** : Adaptabilité sur tous les écrans (desktop, tablette, mobile).

---

## 🔧 Prérequis

- Python 3.x
- Pipenv ou virtualenv pour gérer les environnements virtuels.

---

## 🚀 Installation

1. **Clonez le dépôt :**
   ```bash
   git clone <lien_du_dépôt>
   cd Wawel-main
   ```

2. **Créez et activez un environnement virtuel :**
   ```bash
   python -m venv env
   source env/bin/activate # sous Windows : env\Scripts\activate
   ```

3. **Installez les dépendances :**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurez les variables d'environnement dans un fichier `.env` :**
   ```env
   SECRET_KEY='votre_clé_secrète_django'
   DEBUG=True
   EMAIL_HOST_USER='votre_email@gmail.com'
   EMAIL_HOST_PASSWORD='votre_mot_de_passe'
   ```

5. **Appliquez les migrations de la base de données :**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Lancez le serveur de développement :**
   ```bash
   python manage.py runserver
   ```

7. **Accédez au site dans votre navigateur à :**
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Structure du projet

- **`templates/`** : Contient les fichiers HTML.
- **`static/`** : Contient les fichiers CSS, JavaScript et les images.
- **`models.py`** : Définit les modèles pour les produits, clients, promotions, etc.
- **`views.py`** : Gère la logique des pages et des interactions utilisateur.
- **`forms.py`** : Définit les formulaires pour les produits et promotions.
- **`urls.py`** : Configure les routes du site.

---

## 🛠️ Fonctionnalités à venir

- Intégration d'un système de commande en ligne.
- Ajout d'une page **Blog** pour partager des recettes et des conseils pâtissiers.
- Notifications par e-mail pour les promotions spéciales.

---

## 📞 Contact et Coordonnées

**Boutique Wawel**  
📍 2543 Rue Ontario E, Montréal  
📞 Téléphone : +1 514-123-4567  
📧 Email : [info@wawelpatisseries.com](mailto:info@wawelpatisseries.com)

Suivez-nous sur nos réseaux sociaux :  
- [Facebook](https://www.facebook.com)  
- [Instagram](https://www.instagram.com)  
- [WhatsApp](https://wa.me/1234567890)

---

## ✍️ Auteur

Ce projet a été réalisé par :  
**Ines Oubabas**

N'hésitez pas à me contacter pour toute suggestion ou question concernant ce projet.

---

## 📝 Licence

Ce projet est sous licence [MIT](https://opensource.org/licenses/MIT).  
Vous êtes libre de l'utiliser et de le modifier à votre convenance.
```

Vous pouvez utiliser ce contenu comme votre fichier `README.md`. Copiez-le dans un éditeur de texte ou directement dans votre fichier pour l'intégrer au projet.