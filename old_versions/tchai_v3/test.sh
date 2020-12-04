#!/bin/bash


# RAZ de la BdD
sqlite3 database.db < schema.sql


# Ajout des utilisateurs
curl localhost:5000/user -d '{"username": "Steven", "amount": "12000"}'
curl localhost:5000/user -d '{"username": "Florian", "amount": "0"}'
curl localhost:5000/user -d '{"username": "Sergey", "amount": "1000"}'


# Ajout de transactions
curl localhost:5000/transaction -d '{"user1": "Steven", "user2":"Florian", "amount": "10"}'
curl localhost:5000/transaction -d '{"user1": "Steven", "user2":"Sergey", "amount": "50"}'
curl localhost:5000/transaction -d '{"user1": "Sergey", "user2":"Florian", "amount": "40"}'
curl localhost:5000/transaction -d '{"user1": "Florian", "user2":"Steven", "amount": "10"}'
curl localhost:5000/transaction -d '{"user1": "Florian", "user2":"Sergey", "amount": "28"}'

# Affichage des tables
echo '###########################'
echo 'Liste des utilisateurs'
echo '###########################'
curl localhost:5000/retrieve_users
echo '###########################'
echo 'Liste des transactions:'
echo '###########################'
curl localhost:5000/retrieve_transactions
echo '###########################'
echo 'Les transactions de Sergey:'
echo '###########################'
curl localhost:5000/retrieve_transactions?username=Sergey


echo '###########################'
echo '# Test intégrité BDD      #'
echo 'les requetes suivantes ne sont pas viables (rien ne s affiche si ca fonctionne):'
echo '###########################'
# Test d'intégrité
curl localhost:5000/check_transactions


echo '###########################'
echo 'Attaque:'
echo '###########################'
python3 attack.py


