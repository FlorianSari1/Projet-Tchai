from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import base64
import requests


def make_transaction(user1, user2, amount):


	# Encode le message
	message = user1+user2+amount
	digest = SHA256.new()
	message = message.encode('utf-8')
	digest.update(message)


	# Recupération clé privée
	private_key = RSA.importKey(open(user1+'.pem').read())

	# Signer le message
	signer = PKCS1_v1_5.new(private_key)
	sig = signer.sign(digest)

	encodedBytes = base64.b64encode(sig)
	signature_enc = str(encodedBytes, "utf-8")

	# Execution requete vers serveur
	url = 'http://localhost:5000/transaction'
	data = '{"user1": "'+user1+'", "user2":"'+user2+'", "amount": "'+amount+'", "signature":"'+  signature_enc  +'"}'

	x = requests.post(url, data = data)

	print(x.text)

	


if __name__ == '__main__':

	make_transaction('Steven', 'Florian', '20')
	make_transaction('Sergey', 'Florian', '50')
	make_transaction('Florian', 'Steven', '250')
	
