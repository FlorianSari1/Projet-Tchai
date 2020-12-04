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

from time import gmtime, strftime
def insert_transaction(user1, user2, amount):
	con = sql.connect("database.db")
	cur = con.cursor()
	hash_data = str(user1)+str(user2)+str(float(amount))+str(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
	#print(hash_data)
	h = hashlib.sha256(hash_data.encode('utf-8')).hexdigest()
	cur.execute("INSERT INTO transactions (amount, user1, user2, hash) VALUES (?,?,?,?)", (amount, user1, user2,h))
	con.commit()
	con.close()


def retrieve_transactions():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT * FROM transactions")
	transactions = cur.fetchall()
	check_hash()
	con.close()
	return transactions

def check_hash():
	rep = True
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT *FROM transactions")
	transactions = cur.fetchall()
	for row in transactions:
		h = row[5]
		ck_data = str(row[3])+str(row[4])+str(row[1])+str(row[2])
		#print(ck_data)
		ck_hash = hashlib.sha256(ck_data.encode('utf-8')).hexdigest()
		print('hash : ', h)
		print('new hash : ', ck_hash)
		if h != ck_hash:
			rep = False
	return rep


