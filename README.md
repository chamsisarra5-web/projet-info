# Régularité des TGV en France

## 1. Présentation du projet

Ce projet analyse les facteurs associés à la régularité des TGV en France à partir des données publiques de la SNCF.

L’objectif est double :

- décrire les grandes tendances de la ponctualité des TGV ;
- identifier les variables les plus influentes grâce à une modélisation statistique.

L’analyse porte notamment sur :

- les lignes ferroviaires ;
- la temporalité (année, mois, saison) ;
- le trafic ;
- les causes de retard.

## 2. Comment lancer le projet
Cloner le repository :
```bash
git clone https://github.com/chamsisarra5-web/projet-info.git
cd projet-info
```
Installer les dépendances :
```bash
pip install -r requirements.txt
```
Lancer le notebook :
```bash
jupyter notebook projet_tgv.ipynb
```

## 3. Données
### Source

Les données proviennent de la plateforme open data de la SNCF :

Dataset : Régularité mensuelle des TGV
Accès via API :
https://ressources.data.sncf.com/api/explore/v2.1/catalog/datasets/regularite-mensuelle-tgv-aqst/exports/csv

### Méthode de récupération

Les données ne sont pas stockées dans le repository.  
Elles sont récupérées dynamiquement via l’API open data de la SNCF avec la bibliothèque requests, puis chargées avec pandas.

### Variables principales
| Variable | Description |
|----------|------------|
| date | Mois d’observation |
| service | Type de service (National / International) |
| gare_depart | Gare de départ |
| gare_arrivee | Gare d’arrivée |
| duree_moyenne | Durée moyenne du trajet |
| nb_train_prevu | Nombre de trains prévus |
| nb_annulation | Nombre de trains annulés |
| nb_train_retard_arrivee | Nombre de trains en retard à l’arrivée |
| prct_cause_externe | Causes externes |
| prct_cause_infra | Infrastructure |
| prct_cause_gestion_trafic | Gestion du trafic |
| prct_cause_materiel_roulant | Matériel roulant |
| prct_cause_gestion_gare | Gestion des gares |
| prct_cause_prise_en_charge_voyageurs | Voyageurs |


## 4. Analyse descriptive

L’analyse montre que :

- la régularité des TGV est globalement élevée (entre 75 % et 95 %) ;
- une amélioration est observée entre 2018 et 2021, suivie d’une légère baisse ;
- une saisonnalité existe, avec une baisse en été (fort trafic) ;
- certaines lignes sont significativement plus régulières que d’autres ;
- les trajets internationaux sont légèrement moins réguliers que les trajets nationaux.

Les corrélations entre causes de retard et régularité restent faibles individuellement, ce qui suggère un phénomène multifactoriel.


## 5. Choix du modèle

Un modèle de type Random Forest a été retenu.

Justification:
- capacité à capturer des relations non linéaires ;
- bonne gestion des variables catégorielles (notamment la variable ligne) ;
- meilleures performances que la régression linéaire sur ce jeu de données.
Performances:
- MAE : 0.0399
- RMSE : 0.0641
- R² : 0.43
Résultats principaux:

Les variables les plus importantes sont :

- la gestion du trafic ;
- les causes externes ;
- la durée du trajet ;
- le volume de circulations.


## 6. Conclusion
La régularité des TGV dépend d’un ensemble de facteurs interdépendants.
Les causes opérationnelles et externes jouent un rôle majeur, ce qui souligne la complexité de la gestion du transport ferroviaire.