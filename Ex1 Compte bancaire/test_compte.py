import unittest
from Ex1_compte import *

class test_dépots(unittest.TestCase): 
    # doit fonctionner, on utilise un assertEqual
    def test_depot_montant(self):
        c1 = CompteBancaire("Steve", 20000)
        c1.deposer(100)
        self.assertEqual(20100,c1.balance)
    # doit soulever une erreur de type ValueError (Vous allez devoir retourner dans le code pour que ce soit le cas)
    def test_depot_negatif(self):
        with self.assertRaises(ValueError):
            c1 = CompteBancaire("Steve", 20000)
            c1.deposer(-100)

class test_retraits(unittest.TestCase):
    # effectuer plusieurs assert
    # retirer une petite somme et faites un assertEqual
    # retirer le reste de la balance et faites un assertEqual, la balance devrait être de 0
    def test_retrait_limite(self):
        pass

    def test_retrait_trop_grand(self):
        pass

# Attention ! Vous aurez besoin d'ajouter une fonction setUp et une fonction takeDown pour que ces tests fonctionnent.
class test_transactions(unittest.TestCase):
    # effectuer 1 transaction et vérifier (assert) la longueur de la variable de classe liste_transaction
    # vérifier que le montant contenu dans la première valeur de la liste correspond au montant de votre transaction
    def test_1_transaction(self):
        pass
    
    # faites 2 dépôts et 2 retraits.
    # vérifier : le montant final de la balance, la longueur de liste_transaction, le montant des transactions enregistré.
    def test_4_transactions(self):
        pass

if __name__ == "__main__" :
    unittest.main(verbosity=2)