import hashlib

class RatonCoinBlock:

	def __init__(self, ancien_block_hash, liste_transaction):
		self.ancien_block_hashs = ancien_block_hash
		self.transaction_list = liste_transaction

		self.donnee_block = f"{' - '.join(liste_transaction)} - {ancien_block_hash}"
		self.block_hash = hashlib.sha256(self.donnee_block.encode()).hexdigest()

t1 = "Dorian sends 5 RC to Matheo"
t2 = "Matheo sends 2.3 RC to Angele"
t3 = "Angele sends 4.2 RC to Magali"
t4 = "Loic sends 1.1 RC to Wilfried"

block1 = RatonCoinBlock('firstblock', [t1, t2])

print(f"Block 1 data: {block1.donnee_block}")
print(f"Block 1 hash: {block1.block_hash}")

block2 = RatonCoinBlock(block1.block_hash, [t3, t4]) #On utilise le hash du block h1 pour hasher le deuxieme block

print(f"Block 2 data: {block2.donnee_block}")
print(f"Block 2 hash: {block2.block_hash}")