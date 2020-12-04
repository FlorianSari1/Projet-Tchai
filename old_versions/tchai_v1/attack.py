import sqlite3 as sql
import database as db



def attack_tchai_v1():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("UPDATE transactions SET amount=12 WHERE id=1")
	con.commit()
	con.close()


if __name__ == '__main__':

	attack_tchai_v1()
