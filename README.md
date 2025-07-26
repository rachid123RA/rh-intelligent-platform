# 💼 RH Intelligent Platform

## 📌 Présentation du projet

`rh-intelligent-platform` est une plateforme web intelligente conçue pour aider les départements RH à **automatiser le traitement des candidatures** et à **faciliter la gestion interne des employés** dans les grandes entreprises.

Cette solution permet :

- aux candidats de postuler via le site web ou email,
- au système de **filtrer automatiquement les CV** en fonction d’une offre d’emploi,
- de **classer les meilleurs profils** à l’aide d’un modèle d’IA basé sur le NLP,
- au RH de gérer les **salaires**, **absences**, **primes**, **performances**, **droits**, et de répondre automatiquement aux demandes des employés via un **chatbot intégré**.

---

## 🌟 Fonctionnalités principales

### 🔹 1. Traitement intelligent des CV
- Lecture automatique des CV PDF
- Extraction de données via NLP
- Matching intelligent avec l’offre d’emploi
- Classement des meilleurs profils (Top N)

### 🔹 2. Gestion interne RH
- Gestion des salaires, primes et absences
- Calcul automatique des droits des employés
- Suivi des réclamations et des performances
- Système de points et de décisions RH

### 🔹 3. Chatbot intelligent (Web & WhatsApp)
- Consultation du profil personnel
- Requête de documents (attestation, congé, etc.)
- Réponses automatiques aux questions fréquentes

### 🔹 4. Envoi de mails automatiques (SMTP)
- Notifications de masse pour les fêtes, annonces RH, etc.

---

## 🏗️ Architecture du projet

rh-intelligent-platform/
├── backend/ # Backend Flask (API)
│ ├── routes/ # Endpoints API (upload, match, scoring, etc.)
│ ├── models/ # Modèles de données et CV
│ ├── services/ # Services NLP, parsing PDF, scoring IA
│ └── app.py # Point d’entrée principal de l’API Flask
│
├── frontend/ # Frontend React
│ ├── src/
│ │ ├── screens/ # Pages (Accueil, RH Dashboard, Services, etc.)
│ │ ├── components/ # Composants réutilisables
│ │ └── App.js # Composant racine
│
├── chatbot/
│ ├── rasa/ # Chatbot interne RH via Rasa
│ └── whatsapp_bot/ # Intégration Twilio / WhatsApp
│
├── data/ # Dataset CV + offres d'emploi
├── uploads/ # CV téléchargés
├── .gitignore # Fichiers à ignorer dans Git
├── docker-compose.yml # Déploiement multi-services
└── README.md # Ce fichier

yaml
Copier
Modifier

---

## 💻 Technologies utilisées

| Composant        | Technologie                     |
|------------------|----------------------------------|
| Backend API      | Flask + Python 3.11              |
| NLP / IA         | `SentenceTransformers`, 
                     `scikit-learn`, `PyMuPDF`,
                      `XGBoost`                       |
| Frontend         | React.js                         |
| Chatbot interne  | Rasa                             |
| Chatbot externe  | Twilio API for WhatsApp          |
| Base de données  | MongoDB / SQLite (selon besoin)  |
| Authentification | JWT (ou Firebase Auth si besoin) |
| Envoi Email      | SMTP via Python `smtplib`        |
| Stockage fichiers| `uploads/`                       |

---

## 📁 Description des dossiers

| Dossier/Fichier          | Rôle                                                                 |
|--------------------------|----------------------------------------------------------------------|
| `backend/routes/`        | Endpoints Flask pour uploader, scorer, filtrer les CV                |
| `backend/models/`        | Classes Python représentant les objets (Candidat, Offre, etc.)       |
| `backend/services/`      | Modules de traitement : NLP, PDF parsing, Matching, Scoring          |
| `chatbot/rasa/`          | Bot Rasa pour les employés internes (salaire, droits, etc.)          |
| `chatbot/whatsapp_bot/`  | Bot WhatsApp connecté à la base RH                                   |
| `frontend/src/screens/`  | Pages React (Accueil, Inscription, Dashboard RH, etc.)               |
| `uploads/`               | Répertoire où les CV sont temporairement enregistrés                 |
| `data/`                  | Dataset d'entraînement et données RH                                 |
| `docker-compose.yml`     | Pour lancer tous les services ensemble (Flask + React + MongoDB)     |
| `.gitignore`             | Ignorer les fichiers comme `.env`, `__pycache__`, `node_modules`     |

---

## 🚀 Lancer le projet localement

### 1. Cloner le dépôt
```bash
git clone https://github.com/rachidait21/rh-intelligent-platform.git
cd rh-intelligent-platform
2. Lancer le backend
bash
Copier
Modifier
cd backend
python -m venv venv
venv\Scripts\activate   # ou source venv/bin/activate sur Linux/Mac
pip install -r requirements.txt
python app.py
3. Lancer le frontend
bash
Copier
Modifier
cd frontend
npm install
npm start
4. Lancer le chatbot
bash
Copier
Modifier
cd chatbot/rasa
rasa run
🔮 Prochaines améliorations
 Ajouter authentification JWT

 Ajouter visualisation des scores IA dans le tableau RH

 Ajouter historique des candidatures

 Connexion au cloud MongoDB Atlas

 Automatiser l’envoi de mails après sélection RH

 Interface d’édition des offres d’emploi

🙋 Auteur
Développé avec ❤️ par Rachid Aitaissa — Étudiant en Intelligence Artificielle & Génie de Données.

Contact : rachid.aitaissa@uit.ac.ma
