#!/bin/bash




# RAZ de la BdD
sqlite3 database.db < schema.sql

# Suppression précédentes clés privées
rm Steven.pem Florian.pem Sergey.pem


# Ajout des utilisateurs
curl localhost:5000/user -d '{"username": "Steven", "amount": "12000"}' >> Steven.pem
curl localhost:5000/user -d '{"username": "Florian", "amount": "0"}'	>> Florian.pem
curl localhost:5000/user -d '{"username": "Sergey", "amount": "1000"}'	>> Sergey.pem



# Ajout de transactions
python3 client.py


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
# Test intégrité
curl localhost:5000/check_transactions



