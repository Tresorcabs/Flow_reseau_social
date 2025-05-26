# 🌊 Flow - Réseau Social

Flow est une plateforme de réseau social moderne inspirée des plus grandes applications sociales, construite avec Django et TailwindCSS.

   ## Preview
   ![Flow Preview](https://i.imgur.com/hkvcFLT.jpg)

## ✨ Fonctionnalités

- 👤 Profils utilisateurs personnalisables
- 📝 Création et partage de posts
- 🖼️ Support des images dans les posts
- 👥 Système de suivi d'utilisateurs
- 💬 Interface moderne et responsive
- ⚡ Temps de chargement optimisé
- 🔒 Authentification sécurisée

## 🚀 Démo en direct


## 🛠️ Technologies utilisées

- **Backend**: Django 5.0
- **Frontend**: TailwindCSS
- **Base de données**: SQLite (développement) / PostgreSQL (production)
- **Stockage**: Django Media Files
- **Authentification**: Django Auth System

## 📋 Prérequis

- Python 3.8+
- pip
- virtualenv (recommandé)

## 🔧 Installation

1. **Cloner le repository**
```bash
git clone https://github.com/votre-username/Flow.git
cd Flow
```

2. **Créer un environnement virtuel**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate  # Windows
```

3. **Installer les dépendances**
```bash
pip install -r requirements.txt
```

4. **Configurer la base de données**
```bash
python manage.py migrate
```

5. **Créer un superutilisateur**
```bash
python manage.py createsuperuser
```

6. **Lancer le serveur de développement**
```bash
python manage.py runserver
```

Le site sera accessible à l'adresse `http://localhost:8000`

## 📁 Structure du projet

```
Flow/
├── core/                 # Application principale
│   ├── models.py        # Modèles de données
│   ├── views.py         # Vues et logique
│   ├── forms.py         # Formulaires
│   └── templates/       # Templates HTML
├── static/              # Fichiers statiques
├── media/               # Fichiers uploadés
└── manage.py           # Script de gestion Django
```

## 🔐 Variables d'environnement

Créez un fichier `.env` à la racine du projet :

```env
DEBUG=True
SECRET_KEY=votre-clé-secrète
DATABASE_URL=sqlite:///db.sqlite3
```

## 🧪 Tests

```bash
python manage.py test
```

## 📝 License

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 👥 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push sur la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📞 Contact

X (twitter) - [@TresorCabs](https://x.com/TresorCabs)

Lien du projet: [https://github.com/TresorCabs/Flow_reseau_social](https://github.com/TresorCabs/Flow_reseau_social)

## 🙏 Remerciements

- [Django](https://www.djangoproject.com/)
- [TailwindCSS](https://tailwindcss.com/)
- [Lucide Icons](https://lucide.dev/) 
