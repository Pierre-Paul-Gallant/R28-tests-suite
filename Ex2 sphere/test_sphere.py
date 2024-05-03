import unittest
from Ex2_sphere import *


class test_instanciation_sphere(unittest.TestCase):
    # instancié un ojet avec un rayon de 0
    # vérifié son rayon et son diamètre
    def test_rayon_valide(self):pass
    # instancié un objet avec un rayon de 0 -> devrait soulevé une erreur de type ValueError
    def test_rayon_0(self):pass
    #  devrait soulevé une erreur de type ValueError
    def test_rayon_negatif(self):pass


class test_setter(unittest.TestCase):
    # essayé de modifié le rayon d'une sphere
    # un premier assert test un valeur valide ( > 0 )
    # un deuxième assert test une valeur de 0
    # un troisième assert avec une valeur négative
    def test_rayon_setter(self): 
        s1 = Sphere(10)
        with self.assertRaises(ValueError):
            s1.rayon = 0
        with self.assertRaises(ValueError):
            s1.rayon = -1

    # devrait soulevé une erreur
    def test_circonference_setter(self):
        pass


# La classe sphère ne comporte pas de paramètres volume et aire.
# Vous devez compléter ces tests AVANT d'implémenter les paramètres volume et sphère.
class tests_TDD(unittest.TestCase):
    # doit vérifier la valeur du volume d'une sphère avec un assertEqual
    def test_volume(self) : self.fail()

    # doit vérifier que le setter du volume va soulever une erreur.
    def test_volume_setter(self): self.fail()

    def test_aire(self): self.fail()

    def test_aire_setter(self) : self.fail()


if __name__ == "__main__" :
    unittest.main(verbosity=2)