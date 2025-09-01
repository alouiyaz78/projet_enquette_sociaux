# Projet d'enquête socio-économique des nouveaux arrivants francophones en Ontario

## Description
Ce projet vise à automatiser la collecte, le traitement et la visualisation des résultats d'une enquête menée auprès des nouveaux arrivants francophones en Ontario. L'objectif est de mieux comprendre leur situation socio-économique, leurs difficultés d'intégration et leurs besoins, tout en fournissant des analyses exploitables via un tableau de bord interactif.

## Objectif
- Collecter des données de manière automatisée via Microsoft Forms et Power Automate.  
- Nettoyer et structurer les données avec Python (ETL).  
- Stocker et visualiser les données dans MongoDB Atlas.  
- Produire des insights pour soutenir la communauté francophone immigrante en Ontario.

## Technologies utilisées
- **Collecte & automatisation :** Microsoft Forms, Power Automate  
- **Traitement de données :** Python (pandas, numpy)  
- **Base de données :** MongoDB Atlas  
- **Visualisation :** MongoDB Charts  

## Workflow / Étapes clés
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

## Résultats
- Tableau de bord interactif montrant les tendances clés de l’intégration des nouveaux arrivants.  
- Données structurées et nettoyées prêtes pour analyses futures.  
- Permet d’identifier des besoins et des améliorations pour la communauté francophone.

## Impact & apprentissages
- Automatisation complète du workflow de collecte et d’analyse.  
- Développement de compétences en Python, ETL, Power Automate et MongoDB.  
- Contribution à la compréhension et au soutien des nouveaux arrivants francophones en Ontario.  

Ce projet vise à collecter et analyser les données d'une enquête en ligne automatisée.  
Voici un aperçu du tableau de bord des résultats obtenus :

<img width="1744" height="2254" alt="image" src="https://github.com/user-attachments/assets/8ee251c9-9c8e-4926-b1dc-a5d99f464241" />

