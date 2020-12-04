import sqlite3 as sql

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
	users = cur.fetchall()
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

	# Update users account amout
	update_user_amount(user1, amount, True)
	update_user_amount(user2, amount, False)

def insert_transaction(user1, user2, amount):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("INSERT INTO transactions (amount, user1, user2) VALUES (?,?, ?)", (amount, user1, user2))
	con.commit()
	con.close()


def retrieve_transactions():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM transactions")
	transactions = cur.fetchall()
	con.close()
	return transactions

