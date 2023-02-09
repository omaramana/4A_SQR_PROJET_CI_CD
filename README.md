# 4A_SQR_PROJET_CI_CD
<p align="center">
  <img src="https://user-images.githubusercontent.com/93181410/166483696-8a4daae2-d6e3-4a61-b425-f5118cc6e085.png" width="700"/>
</p>

*Réalisé par : AMANA OMAR & EL AMRI MOHAMED*
**SQR**

Objectif du projet  : Créer une API Flask pour de la gestion CRUD d’un système de transaction.

Langage utilisé : Python.

[![](https://img.shields.io/badge/PROJET_TERMINÉ_🚀-059142?style=for-the-badge&logoColor=white)](https://dev.to/envoy_/150-badges-for-github-pnk) 

## Partie Exercices 
https://github.com/omaramana

https://github.com/elamrimohamed1

<p align="center">
  <img src="https://miro.medium.com/max/720/1*94uo6-HGPepRG9I0L_Bh7w.webp""width="700"/
  </p>
<p> Nous avons choidi le sujet guidé car nous n'étions pas en capacité de nous lancer dans l'autre sujet moins guidé du fait de notre expérience réduite dans ce genre de projet. Nous avons également choisi le langage de programmation Python car nous sommes habitués à l'utiliser du fait de nomobreux projets réalisés avec ce langage. </p>

![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)

![badge aller sur le site](https://github.com/omaramana/4A_SQR_PROJET_CI_CD/actions/workflows/allerSurLeSite.yml/badge.svg)
![badge echo push](https://github.com/omaramana/4A_SQR_PROJET_CI_CD/actions/workflows/echoNewPush.yml/badge.svg)
![badge pull request](https://github.com/omaramana/4A_SQR_PROJET_CI_CD/actions/workflows/question3.yml/badge.svg)

                                                                                      
## Partie commandes                                                                               
                                                                                      
E1 - Enregistrer une transaction : 
```                                                                             
curl -X GET http://localhost:5555/E1/{id1}/{id2}/{date}/{somme}
```
                                                                               
E2 - Afficher une liste de toutes les transactions dans l’ordre chronologique :
```
curl -X GET http://localhost:5555/listeTransactions                                                                                     
```

E3 - Afficher une liste des transactions dans l’ordre chronologique liées à une personne.
```
curl -X GET http://localhost:5555/listeTransactionPourUnClient/{id}                                                                                   
```
                                                                                      
E4 - Afficher le solde du compte de la personne 
```
curl -X GET http://localhost:5555/soldeUnClient/{id}
```
                                                                                      
E5 - Importer des données depuis un fichier csv
```
curl -X POST -F 'clients=@{file.csv}' http://localhost:5555/importerDepuisCSV/personnes
curl -X POST -F 'transactions=@{file.csv}' http://localhost:5555/importerDepuisCSV/transactions
```
