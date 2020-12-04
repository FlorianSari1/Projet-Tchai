from flask import Flask
from flask import request
import database as db

app = Flask(__name__)


### Users

@app.route('/user', methods=['POST', 'GET'])
def user():
	if request.method=='POST':
		data = request.get_json(force=True)
		print('Data Received: "{data}"'.format(data=data))
		db.insert_user(data['username'], data['amount'])
		return "Request Processed.\n"

@app.route('/retrieve_users', methods=['GET'])
def retrieve_users():
	if request.method=='GET':
		users = data_to_string(db.retrieve_users())	
		return users

### Transactions

@app.route('/transaction', methods=['POST'])
def transaction():
	if request.method=='POST':
		data = request.get_json(force=True)
		db.make_transaction(data['user1'], data['user2'], data['amount'])
		return "Request Processed.\n"

@app.route('/retrieve_transactions', methods=['GET'])
def retrieve_transaction():
	if request.method=='GET':
		username = request.args.get('username')
		if username is not None:
			return data_to_string(db.retrieve_transactions_by_username(username))	
		else:
			return data_to_string(db.retrieve_transactions())	



@app.route('/check_transactions', methods=['GET'])
def check_transactions():
	if request.method=='GET':
		invalid_transactions = db.check_hash_tchai_v3()
		return data_to_string(invalid_transactions)

######################################

def data_to_string(data):
	data_string = ''
	for row in data:
		for col in row:
			data_string += str(col) + ' | '
		data_string += '\n'
	return data_string

######################################

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
