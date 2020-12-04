from time import gmtime, strftime
import sqlite3 as sql
import hashlib


###### USERS

def insert_user(username, amount):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO users (username,amount) VALUES (?,?)", (username,amount))
	con.commit()
	con.close()

def retrieve_user(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT username, amount FROM users WHERE username='?'",(username))
	users = cur.fetchone()
	con.close()
	return user

def retrieve_users():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM users")
	users = cur.fetchall()
	con.close()
	return users

def update_user_amount(username, transaction_amount, add):

	'''	
	Permet de mettre a jour le montant de l'utilisateur, l'argument add est un booléen
	soit on ajoute le montant, soit on l'enleve.
	'''

	con = sql.connect("database.db")
	cur = con.cursor()
	if add:
		cur.execute("UPDATE users SET amount=amount+"+transaction_amount+" WHERE username='"+username+"'")
	else:
		cur.execute("UPDATE users SET amount=amount-"+transaction_amount+" WHERE username='"+username+"'")
	con.commit()
	con.close()
	
	
###### TRANSACTIONS

def make_transaction(user1, user2, amount):
	# Ajout de la transaction dans la bdd
	insert_transaction(user1, user2, amount)
	# Mise à jour des montant des comptes utilisateurs
	update_user_amount(user1, amount, True)
	update_user_amount(user2, amount, False)



def insert_transaction(user1, user2, amount):

	# Connexion BdD
	con = sql.connect("database.db")
	cur = con.cursor()

	time = strftime("%Y-%m-%d %H:%M:%S", gmtime())



	# Récupération du dernier hash
	cur.execute("SELECT hash FROM transactions WHERE id=(SELECT max(id) FROM transactions)")
	last_hash = cur.fetchone()

	# Si la table de transactions est vide
	if last_hash is None:
		last_hash = " "

	# Calcul du hash
	hash_transaction = hash_tchai_v3(last_hash[0], user1, user2, amount, time)
	
	# Ajout transaction BdD
	cur.execute("INSERT INTO transactions (amount, user1, user2, hash) VALUES (?,?,?,?)", (amount, user1, user2,hash_transaction))
	con.commit()
	con.close()


def retrieve_transactions():

	# Connexion BdD
	con = sql.connect("database.db")
	cur = con.cursor()

	# Récupération des transaction
	cur.execute("SELECT * FROM transactions")
	transactions = cur.fetchall()
	con.close()
	return transactions


def retrieve_transactions_by_username(username):

	# Connexion BdD
	con = sql.connect("database.db")
	cur = con.cursor()

	# Récupération des transaction
	cur.execute("SELECT * FROM transactions WHERE user1=? OR user2=?", (username, username))
	transactions = cur.fetchall()
	con.close()
	return transactions


### Hash

def hash_tchai_v3(last_hash, user1, user2, amount, time):


	hash_data = str(user1)+str(user2)+str(float(amount))+str(time) + str(last_hash)
	transaction_hash = hashlib.sha256(hash_data.encode('utf-8')).hexdigest()
	return transaction_hash



def check_hash_tchai_v3():

	invalid_transactions = []

	# Connexion BdD
	con = sql.connect("database.db")
	cur = con.cursor()

	# Récupération de toutes les transactions
	transactions = retrieve_transactions()

	# Vérification intégrité du hash de chaque transaction
	for id, row in enumerate(transactions, start=1):
		actual_hash = row[5]

		if id == 1:
			previous_hash = " "
		else:
			previous_hash = transactions[id-2][5]

		check_hash = hash_tchai_v3(previous_hash, row[3], row[4], row[1], row[2])
		if actual_hash != check_hash:
			invalid_transactions.append(row)
	
	return invalid_transactions
