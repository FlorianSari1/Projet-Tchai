

# TCHAI-Steven-TEL-Florian-SARI


## Installation de l'environnement
### Requirements
 - python 3.7
 ``` shell
sudo apt-get update -y && \
    apt-get install -y python3-pip python3-dev 
```
 - pycrypto 2.6.1
 - Flask 1.1.1
 - SQLAlchemy1.2.19
``` shell
pip3 install requirements.txt
```

### Docker (optional)

- Build docker imagee:

```shell
sudo docker build -t tchaisaritel .
```

- Run the image:

```shell
sudo docker run -p 5000:5000 -ti tchaisaritel 
```
After that you can run the server:
```shell
python3 server.py
```

## Tests

Il est facilement possible de tester les différentes versions en executant les fichiers shell à disposition dans chaque version.

**1 - Lancer le serveur**
``` shell
python3 server.py
```

**2 - Lancer le script de test**
``` shell
sh test.sh
```

Le script shell de test contient la création d'utilisateur, de transaction ainsi que le test d'intégrité de la base de données et les différentes attaques possible pour chaque version.


## Projet TCHAI v1

### Architecture base de données
La base de données est composée de deux tables, une pour les utilisateurs et une pour les transactions. 
Pour ce faire nous avons choisis SQLite pour mettre en place cette base de données, en effet c'est une bibliothèque très utilisée dans le monde et qui implémente un moteur de base de données rapide, fiable et complet.

User: 
 - username (PRIMARY KEY)
 - amount 
 
 Transaction:
 - Id (PRIMARY KEY)
 - amount
 - time
 - user1 (FOREIGN KEY)
 - user2 (FOREIGN KEY)

#### Créer la base de données
sqlites3 database.db < schema.sql

#### Ajouter un utilisateur
curl localhost:5000/user -d '{"username": "steven", "amount": "12000"}'

#### Récupérer la liste des utilisateurs
curl localhost:5000/retrieve_users

#### Récupérer la liste des utilisateur
curl localhost:5000/retrieve_users

#### Récupérer un utilisateur donné
curl localhost:5000/retrieve_user(user_name)
 
#### Attaque v1
L'attaque consiste à changer directement le montant d'une transaction par l'intermédiaire d'une requête sql. Une fois lancée on voit que l'attaque fonctionne et réussit à modifier le montant d'une transaction sans difficulté.

## TCHAI v2

#### Nouvelle structure 
La table transaction intègre désormais une colonne "hash", la base de données augmente donc son niveau de sécurité car il nécessaire d'avoir le hash pour effectuer des modifications sur les transactions.
 - Id (PRIMARY KEY)
 - amount
 - time
 - hash
 - user1 (FOREIGN KEY)
 - user2 (FOREIGN KEY)
 
 On se sert de la méthode sha256 pour calculer les hash car elle offre un bon niveau de sécurité, cette fonction est disponible grâce à la bibliothèque  hashlib.

#### Vérification  de l'intégrité des données
L'intégrité se vérifie en prenant le hash actuel, en le recalculant avec la même méthode de cryptage, lui passant les mêmes paramètres puis regarder si les hash se correspondent. 

#### Attaque
En attaquant le système à nouveau avec l'attaque précédente on remarque que cette dernière ne fonctionne plus car le hash permet de protéger la donnée.
Ensuite on met en place une nouvelle attaque qui supprime une transaction, cette attaque peut entraîner une double dépense car le jeton pour la transaction peut être utilisé plus d'une fois, créant ainsi une "fausse monnaie".

## TCHAI v3
####  Changement du calcul du hash
Le hash se calcule maintenant en rajoutant le hash de la transaction précédente pour le calcul du hash de la transaction actuelle.

#### Attaques
Après l'implémentation de ce nouveau calcul de hash, on ré-attaque le système avec les deux attaques précédentes, on constate qu'elles ne marchent plus. 
On implémente une nouvelle attaque qui insert une nouvelle transaction dans la base de données, on constate que l'attaque fonctionne.

## TCHAI v4
Afin de vérifier l'authenticité des expéditeurs, on met en place un système de clé publique et privé. Un attribut clé publique est ajouté dans la table user pour la mise en place d'un système de signature.

User: 
 - username (PRIMARY KEY)
 - amount 
 - public key

Une clé privée et publique sont générées avec le chiffrement RSA, la clé privée est envoyée au client et stockée dans un fichier .pem, ce type de fichier est spécialement conçu pour lire des clés rsa. Une fois que le client a accès à la clé privée, il peut ensuite signer la transaction, à la reception de la transaction signée, le serveur récupère la clé publique de de l'emetteur de la transaction (premier username dans la transaction), il vérifie ensuite la signature de la transaction, si celle-ci est vérifiée alors la transaction est faite, refusée sinon.

## Auteurs

TEL Steven -- m.steventel@gmail.com
SARI Florian -- florian.sari@gmail.com
