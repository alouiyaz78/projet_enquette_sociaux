# Projet d'enquête socio-économique des nouveaux arrivants francophones en Ontario / Socio-Economic Survey Project for New Francophone Arrivals in Ontario

---

## 🇫🇷 Français

### Description
Ce projet vise à automatiser la collecte, le traitement et la visualisation des résultats d'une enquête menée auprès des nouveaux arrivants francophones en Ontario. L'objectif est de mieux comprendre leur situation socio-économique, leurs difficultés d'intégration et leurs besoins, tout en fournissant des analyses exploitables via un tableau de bord interactif.

### Objectif
- Collecter des données de manière automatisée via Microsoft Forms et Power Automate.
- Nettoyer et structurer les données avec Python (ETL).
- Stocker et visualiser les données dans MongoDB Atlas.
- Produire des insights pour soutenir la communauté francophone immigrante en Ontario.

### Technologies utilisées
- **Collecte & automatisation :** Microsoft Forms, Power Automate  
- **Traitement de données :** Python (pandas, numpy)  
- **Base de données :** MongoDB Atlas  
- **Visualisation :** MongoDB Charts  

### Workflow / Étapes clés
1. **Collecte des données :**
   - Enquête diffusée sur des groupes Facebook et via e-mails.  
   - Participants : 250 réponses obtenues en deux semaines.
2. **Automatisation (Power Automate) :**
   - Formulaire connecté à Excel via un flux automatisé.  
   - Notification automatique de chaque nouvelle réponse à l’équipe projet.
3. **Nettoyage et transformation (Python ETL) :**
   - Suppression des colonnes non pertinentes et gestion des doublons.  
   - Standardisation des noms de pays, provinces et villes.  
   - Conversion en JSON pour insertion dans MongoDB Atlas.
4. **Insertion dans MongoDB Atlas :**
   - Utilisation de `pymongo` pour insérer les données nettoyées.
5. **Visualisation et tableau de bord :**
   - Création de graphiques interactifs (donut, bar, grouped bar) avec MongoDB Charts.  
   - Analyse des situations socio-économiques et des contraintes à l’emploi.

### Résultats
- Tableau de bord interactif montrant les tendances clés de l’intégration des nouveaux arrivants.  
- Données structurées et nettoyées prêtes pour analyses futures.  
- Permet d’identifier des besoins et des améliorations pour la communauté francophone.

### Impact & apprentissages
- Automatisation complète du workflow de collecte et d’analyse.  
- Développement de compétences en Python, ETL, Power Automate et MongoDB.  
- Contribution à la compréhension et au soutien des nouveaux arrivants francophones en Ontario.

---

## 🇬🇧 English

### Description
This project aims to automate the collection, processing, and visualization of survey results conducted among new Francophone arrivals in Ontario. The goal is to better understand their socio-economic situation, integration challenges, and needs, while providing actionable insights via an interactive dashboard.

### Objectives
- Automatically collect data using Microsoft Forms and Power Automate.  
- Clean and structure data with Python (ETL).  
- Store and visualize data in MongoDB Atlas.  
- Generate insights to support the Francophone immigrant community in Ontario.

### Technologies Used
- **Collection & Automation:** Microsoft Forms, Power Automate  
- **Data Processing:** Python (pandas, numpy)  
- **Database:** MongoDB Atlas  
- **Visualization:** MongoDB Charts  

### Workflow / Key Steps
1. **Data Collection:**
   - Survey shared on Facebook groups and via email.  
   - Participants: 250 responses obtained in two weeks.
2. **Automation (Power Automate):**
   - Form connected to Excel through an automated flow.  
   - Automatic notification of each new response to the project team.
3. **Cleaning & Transformation (Python ETL):**
   - Remove irrelevant columns and handle duplicates.  
   - Standardize country, province, and city names.  
   - Convert to JSON for insertion into MongoDB Atlas.
4. **Insertion into MongoDB Atlas:**
   - Use `pymongo` to insert cleaned data.
5. **Visualization & Dashboard:**
   - Create interactive charts (donut, bar, grouped bar) using MongoDB Charts.  
   - Analyze socio-economic situations and employment constraints.

### Results
- Interactive dashboard showing key trends in new arrivals’ integration.  
- Structured and cleaned data ready for future analysis.  
- Identify needs and areas for improvement for the Francophone community.

### Impact & Learnings
- Full automation of the data collection and analysis workflow.  
- Developed skills in Python, ETL, Power Automate, and MongoDB.  
- Contributed to understanding and supporting new Francophone arrivals in Ontario.

---

**Tableau de bord aperçu / Dashboard Preview:**  
![Aperçu du tableau de bord](lien_vers_image.png)


<img width="1744" height="2254" alt="image" src="https://github.com/user-attachments/assets/8ee251c9-9c8e-4926-b1dc-a5d99f464241" />

