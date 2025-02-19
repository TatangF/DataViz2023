# DataViz Challenge : Analyse et IA

## Recensement Agricole Européen 2020 : Cas du Pays Basque

### Objectif du Challenge
Retrouvez les détails du challenge sur la plateforme ZABAL Open Data [ICI](https://zabal-agriculture.opendata-paysbasque.fr/explore/dataset/rga-2020-dataviz-challenge-copie/information/?disjunctive.echelle&disjunctive.categorie&disjunctive.type&disjunctive.annee&disjunctive.age_5&dataChart=eyJxdWVyaWVzIjpbeyJjb25maWciOnsiZGF0YXNldCI6InJnYS0yMDIwLWRhdGF2aXotY2hhbGxlbmdlLWNvcGllIiwib3B0aW9ucyI6eyJkaXNqdW5jdGl2ZS5lY2hlbGxlIjp0cnVlLCJkaXNqdW5jdGl2ZS5jYXRlZ29yaWUiOnRydWUsImRpc2p1bmN0aXZlLnR5cGUiOnRydWUsImRpc2p1bmN0aXZlLmFubmVlIjp0cnVlLCJkaXNqdW5jdGl2ZS5hZ2VfNSI6dHJ1ZX19LCJjaGFydHMiOlt7ImFsaWduTW9udGgiOnRydWUsInR5cGUiOiJjb2x1bW4iLCJmdW5jIjoiQVZHIiwieUF4aXMiOiJ2YWxldXIiLCJzY2llbnRpZmljRGlzcGxheSI6dHJ1ZSwiY29sb3IiOiIjQ0EzMjM0In1dLCJ4QXhpcyI6ImVjaGVsbGUiLCJtYXhwb2ludHMiOjUwLCJzb3J0IjoiIn1dLCJ0aW1lc2NhbGUiOiIiLCJkaXNwbGF5TGVnZW5kIjp0cnVlLCJhbGlnbk1vbnRoIjp0cnVlfQ%3D%3D&location=9,43.24981,-1.26903&basemap=jawg.streets).

## Installation et Exécution
1. Clonez le projet :
   ```bash
   git clone https://github.com/TatangF/DataViz2023.git
   cd DataViz2023
   ```
2. Configurez et exécutez Uvicorn :
   - Ouvrez `runtime.txt`
   - Exécutez la commande en Bash à partir de la deuxième ligne.

### Rapport du Projet
Consultez et téléchargez le rapport détaillé [ICI](https://github.com/TatangF/DataViz2023/blob/master/Rapport_DataViz_Tatang_Fomekon_Ferol_2023.pdf).

## Projet : Prédiction et Visualisation des Rendements Agricoles au Pays Basque

### Technologies Utilisées
- **Langage** : Python
- **Bibliothèques** : Scikit-Learn, Pandas, Matplotlib, Seaborn, Plotly
- **Développement et Déploiement** : FastAPI, Streamlit, Postman

## Contexte
L’objectif du projet est d’analyser les données agricoles du Pays Basque (issues de ZABAL Open Data) afin d’identifier les facteurs influençant la production agricole et de prédire les rendements futurs.

## Réalisations

### 1. Nettoyage et Préparation des Données
- Gestion des valeurs manquantes (remplacement par la moyenne, médiane, ou valeurs fréquentes).
- Normalisation des données numériques et encodage des variables catégorielles (One-Hot Encoding).
- Analyse exploratoire (EDA) pour identifier les corrélations entre les variables (superficie agricole, unités de bétail, etc.).

### 2. Modélisation et Prédiction
- Conception d’un pipeline de Machine Learning utilisant **Random Forest Regression**.
- Prédiction des rendements agricoles avec une précision de **89,17%**.
- Comparaison avec d’autres modèles (Régression Linéaire, Ridge) pour valider les performances.

### 3. Visualisation et Déploiement
- Création de **graphiques interactifs** avec Matplotlib, Seaborn et Plotly.
- Développement d’une **API FastAPI** pour servir le modèle et permettre des prédictions en temps réel.
- Tests de l’API via Postman et **déploiement d’une interface utilisateur avec Streamlit**.

### 4. Optimisation
- **Réduction de 30%** du temps de traitement des données grâce à l’optimisation des pipelines ETL.
- Utilisation de **techniques NLP (TF-IDF, similarité cosinus)** pour analyser les données textuelles liées aux exploitations agricoles.

## Résultats
- **Identification des facteurs clés** influençant la production agricole : superficie agricole, unités de bétail, et temps de travail.
- **Prédiction précise des rendements agricoles** pour aider à la planification stratégique.
- **Visualisation claire des tendances historiques et des projections futures**.

## Distinction
Je suis fier d’avoir été **finaliste du Dataviz Challenge 2023** ! 🎉
Retrouvez les résultats officiels [ICI](https://agriculture-opendatapaysbasque.opendatasoft.com/pages/datavizchallengeresultat/).

## Compétences Mobilisées
- **Data Cleaning**, **EDA**, **Machine Learning** (Scikit-Learn).
- **Data Visualization** (Matplotlib, Seaborn, Plotly).
- **Développement d’API** (FastAPI), **tests** (Postman), **déploiement d’applications** (Streamlit).
- **Optimisation des pipelines de données** et **utilisation de techniques NLP**.

---

N’hésitez pas à contribuer et à explorer ce projet ! 🚀

