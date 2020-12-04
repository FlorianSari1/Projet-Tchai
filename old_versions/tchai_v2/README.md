
# TCHAI-Steven-TEL-Florian-SARI


## Projet TCHAI v1

### Architecture base de données

Personne: 
 - username (PRIMARY KEY)
 - amount 
 
 Transaction:
 - Id (PRIMARY KEY)
 - amount
 - time
 - user1 (FOREIGN KEY)
 - user2 (FOREIGN KEY)

### Test 

#### Créer la base de données
sqlites3 database.db < schema.sql

#### Ajouter un utilisateur
curl localhost:5000/user -d '{"username": "steven", "amount": "12000"}'

#### Récupérer la liste des utilisateurs
curl localhost:5000/retrieve_users


## TCHAI v2

## TCHAI v3

## TCHAI v4

## Heading Auteur

TEL Steven -- m.steventel@gmail.com
SARI Florian -- florian.sari@gmail.com
