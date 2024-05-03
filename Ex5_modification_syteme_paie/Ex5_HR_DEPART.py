#On veut calculer la paie des employes
#Mais on a des employés payés à la semaine pour un montant fixe
#On a aussi des employés payés à la semaine pour un montant fixe ET qui ont aussi une commission 
#On a aussi des employés payés à l'heure

from abc import ABC,abstractmethod

class Systeme_de_paie:
    def calculer_paie(self, employes):
        print("Calcul de la paie des employes")
        print("==============================")
        for employe in employes:
            print(f'Paie de: {employe.id} - {employe.nom}')
            print(f' - montant net de:  {employe.calculer_paie()}')
            print('')
            
class Employe(ABC):
    
    liste_employes = []
    
    def __init__(self, id, nom):
        self.id = id
        self.nom = nom
        Employe.liste_employes.append(self)
        
    @abstractmethod
    def calculer_paie():
        pass
    
    
class Employe_salarie(Employe):
    def __init__(self, id, nom, salaire_par_semaine):
        super().__init__(id, nom)
        self._salaire_par_semaine = salaire_par_semaine
    
    @property
    def salaire_par_semaine(self) :
        return self._salaire_par_semaine
    @salaire_par_semaine.setter
    def salaire_par_semaine(self, nouveau_salaire) :
        try :
            nouveau_salaire = float(nouveau_salaire)
            self._salaire_par_semaine = nouveau_salaire
            print(f"Le nouveau salaire de {self.nom} est de : {self._salaire_par_semaine} par semaine.")
        except :
            print(f"Le salaire de {self.nom} n'a pas pu être changer.")

    def calculer_paie(self):
        return self.salaire_par_semaine
 
class Employe_heure(Employe):  
    def __init__(self, id, nom, heures_travaillees, taux_horaire):
        super().__init__(id, nom)
        self._heures_travaillees = heures_travaillees
        self._taux_horaire = taux_horaire
    
    @property
    def heures_travaillees(self) : return self._heures_travaillees
    @heures_travaillees.setter
    def heures_travaillees(self, nvl_heures) :
        try :
            self._heures_travaillees = float(nvl_heures)
            print(f"Les nouvelles heures de {self.nom} est de : {self._heures_travaillees} par semaine.")
        except : print(f"Les heures de {self.nom} n'on pas pu être changer.")

    @property
    def taux_horaire(self): return self._taux_horaire
    @taux_horaire.setter
    def taux_horaire(self, nvx_taux):
        try :
            self._taux_horaire = float(nvx_taux)
            print(f"Le nouveau taux de {self.nom} est de : {self._taux_horaire} par semaine.")
        except : print(f"Le salaire de {self.nom} n'a pas pu être changer.")


    def calculer_paie(self):
        return self.heures_travaillees * self.taux_horaire
    
class Employe_commission(Employe_salarie):  
    def __init__(self, id, nom, salaire_par_semaine, commission):
        super().__init__(id, nom, salaire_par_semaine)
        self._commission = commission

    @property
    def commission(self): return self._commission
    @commission.setter
    def commission(self, new_commision):
        try :
            self._commission = float(new_commision)
            print(f"Le nouveau taux de {self.nom} est de : {self._commission} par semaine.")
        except : print(f"Le salaire de {self.nom} n'a pas pu être changer.")

    def calculer_paie(self):
        salaire_fixe = super().calculer_paie()
        return salaire_fixe + self.commission


if __name__ == '__main__' :

    employe_salarie1 = Employe_salarie(1, 'Marc Tremblay', 2100)
    employe_heure1 = Employe_heure(2,'Pierre Jonhson', 40, 22)
    employe_commission1 = Employe_commission(3, 'Luc Toupin', 1400, 600)
    #employex = Employe(4,'Lucie Rangers')


    systeme_de_paie_hr = Systeme_de_paie()
    systeme_de_paie_hr.calculer_paie([employe_salarie1,employe_heure1,employe_commission1])


    
     