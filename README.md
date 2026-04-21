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

##  Contenu du dépôt

- `projet_tgv.ipynb` : notebook principal contenant le chargement des données, le nettoyage, l’analyse descriptive, les visualisations et la modélisation ;
- `utils.py` : fonctions utilitaires utilisées dans le projet, notamment pour la création des saisons et certains graphiques ;
- `requirements.txt` : liste des bibliothèques nécessaires à l’exécution du projet ;
- `README.md` : présentation du projet, des données et des consignes d’exécution.

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

Puis ouvrir le notebook Jupyter et exécuter l’ensemble des cellules (Run all).



## 3. Données
### Source

Les données proviennent de la plateforme open data de la SNCF, via l’API du jeu de données **Régularité mensuelle des TGV**.


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
| nb_train_prevu | Nombre de trains prévus sur la liaison et pour le mois considérés |
| nb_annulation | Nombre de trains annulés parmi les trains prévus |
| nb_train_retard_arrivee | Nombre de trains arrivés en retard |
| prct_cause_externe | Part des retards attribuée à des causes externes à l’exploitation ferroviaire |
| prct_cause_infra | Part des retards attribuée à des problèmes d’infrastructure |
| prct_cause_gestion_trafic | Part des retards attribuée à la gestion du trafic ferroviaire |
| prct_cause_materiel_roulant | Part des retards attribuée à des problèmes de matériel roulant |
| prct_cause_gestion_gare | Part des retards attribuée à la gestion en gare |
| prct_cause_prise_en_charge_voyageurs | Part des retards attribuée à la prise en charge des voyageurs |

### Variables construites

Dans le cadre du prétraitement, plusieurs variables ont été créées à partir des données brutes :

- `annee` : année d’observation extraite de la date ;
- `mois` : mois d’observation ;
- `saison` : saison associée au mois ;
- `ligne` : liaison ferroviaire construite à partir de la gare de départ et de la gare d’arrivée ;
- `circulations_effectives` : nombre de trains effectivement circulés, calculé comme `nb_train_prevu - nb_annulation` ;
- `taux_annulation` : part des trains annulés parmi les trains prévus ;
- `regularite_arrivee` : proportion de trains arrivés sans retard parmi les circulations effectivement réalisées.

Ces variables permettent de mieux décrire les conditions d’exploitation des lignes et de construire une mesure cohérente de la régularité à l’arrivée.

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
- MAE : 0.0401
- RMSE : 0.0647
- R² : 0.4225
Résultats principaux :

Les variables les plus influentes sont :

- la ligne ferroviaire ;
- le volume de circulations prévues ;
- la gestion du trafic ;
- les causes externes ;
- la durée moyenne du trajet ;
- le taux d’annulation.


## 6. Conclusion

La régularité des TGV dépend d’un ensemble de facteurs interdépendants.  
L’analyse montre que la liaison ferroviaire, le volume de circulations, la gestion du trafic, les causes externes, la durée du trajet et le taux d’annulation jouent un rôle important.  
Ces résultats soulignent la complexité de la ponctualité ferroviaire, qui dépend à la fois de caractéristiques propres aux lignes, de facteurs opérationnels et de contraintes externes.