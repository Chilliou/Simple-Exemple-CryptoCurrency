from RatonCoinBlock import RatonCoinBlock


class Blockchain:
	def __init__(self):
		self.chain = []
		self.generer_block_originel()

	def generer_block_originel(self):
		self.chain.append(RatonCoinBlock("0", ['Block Originel']))

	def creer_un_block_depuis_une_transaction(self, liste_transaction):
		ancien_block_hash = self.dernier_block.block_hash
		self.chain.append(RatonCoinBlock(ancien_block_hash, liste_transaction))

	def afficher_chain(self):
		for i in range(len(self.chain)):
			print(f"Donnée {i + 1}: {self.chain[i].donnee_block}")
			print(f"Hash {i + 1}: {self.chain[i].block_hash}\n")

	@property
	def dernier_block(self):
		return self.chain[-1]