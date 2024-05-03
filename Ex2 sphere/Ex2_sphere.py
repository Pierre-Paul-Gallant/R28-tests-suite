from math import pi

class Sphere:
    def __init__(self, pRayon) -> None:
        #if type(pRayon) != int and type(pRayon) :
        #    raise TypeError("Le raon doit être de type <int>. type fourni :",type(pRayon)) 
        #if pRayon <= 0 :
        #    raise ValueError("Le rayon doit avoir une valeur positive. Valeur fourni:",pRayon)
        self._rayon = 0
        self.rayon = pRayon # NOTE Les lignes précédentes ne sont pas nécessaire, la vérification à été mise dans le rayon.setter
    
    @property
    def rayon(self) :
        return self._rayon
    
    @rayon.setter
    def rayon(self, pRayon):
        if type(pRayon) != int and type(pRayon) != float:
            raise TypeError("Le rayon doit être de type <int>. type fourni :",type(pRayon)) 
        if pRayon <= 0 :
            raise ValueError("Le rayon doit avoir une valeur positive. Valeur fourni:",pRayon)
        self._rayon = pRayon

    @property
    def circonference(self):
        return 2 * pi * self._rayon # la circonférence d'une sphère est égal à " 2 * pi * rayon "



if __name__ == "__main__" :
    print(pi) #voyez que vous pouvez utilisé la constante pi
    try : s1 = Sphere(-10)
    except ValueError: print("Impossible de faire une sphere avec un rayon de -10")

    try : s2 = Sphere("cinq")
    except TypeError: print("Impossible de faire une sphere avec un rayon de 'cinq'")
    
        

    s3 = Sphere(20)

    try : s3.rayon = -10
    except ValueError: print("Impossible de changer un rayon pour -10")

    try : s3.rayon = "cinq"
    except TypeError: print("Impossible de changer un rayon pour 'cinq'")
    
    print("\nValeurs de s3 : ")
    print("rayon:",s3.rayon," circ:",s3.circonference," vol:")

    s3.rayon = 10
    print("\nOn change le rayon pour 10 : ")
    print("rayon:",s3.rayon," circ:",s3.circonference," vol:","\n")


    #Testez votre code, voir l'énoncé

