from BlockChain import Blockchain

t1 = "Matheo envoie 3.1 RC à Dorian"
t2 = "Henri envoie 2.5 RC à Wilfried"
t3 = "Noe envoie 1.2 RC à Aymeric"
t4 = "Axel envoie 0.5 RC à Line"
t5 = "Anthonin envoie 0.2 RC à Magali"
t6 = "Theo envoie 0.1 RC à Loic"

maBlockchain = Blockchain()

maBlockchain.creer_un_block_depuis_une_transaction([t1, t2])
maBlockchain.creer_un_block_depuis_une_transaction([t3, t4])
maBlockchain.creer_un_block_depuis_une_transaction([t5, t6])

maBlockchain.afficher_chain()