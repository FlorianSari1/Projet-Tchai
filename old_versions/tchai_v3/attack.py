import sqlite3 as sql
import database as db



def attack_tchai_v2():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("UPDATE transactions SET amount=12 WHERE id=1")
	con.commit()
	con.close()



def attack_tchai_v3():
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("DELETE FROM transactions WHERE _rowid_ IN ('2')")
	con.commit()
	con.close()


if __name__ == '__main__':

	attack_tchai_v3()


	if len(db.check_hash_tchai_v3()) == 0:
		print("L'attaque a fonctionné !")
	else:
		print("L'attaque n'a pas fonctionné !")
