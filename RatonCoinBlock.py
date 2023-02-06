import hashlib

class RatonCoinBlock:

	def __init__(self, ancien_block_hash, liste_transaction):
		self.ancien_block_hash = ancien_block_hash
		self.transaction_list = liste_transaction

		self.donnee_block = f"{' - '.join(liste_transaction)} - {ancien_block_hash}"
		self.block_hash = hashlib.sha256(self.donnee_block.encode()).hexdigest()
