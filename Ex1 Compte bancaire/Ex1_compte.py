from datetime import datetime

class CompteBancaire :
      liste_transaction = []
      def __init__(self, compte_holder, balance=0) :
            self.compte_holder = compte_holder
            self.balance = balance

      def deposer(self,montant):
            self.balance += montant
            self.liste_transaction.append(f"heure {self.__temps_maintenant()} 'Dépot de {montant}$")
    
      def retirer(self,montant):
            if montant > self.balance :
                  raise ValueError(f"Montant ({montant}) > Balance({self.balance})")
            self.balance -= montant
            self.liste_transaction.append((f"heure {self.__temps_maintenant()} 'Retrait de {montant}$"))
            
            print(f"Le retrait de {montant} à été effectué.")
            print(f"Votre balance est maintenant de {self.balance} $")
      
      @classmethod
      def imprimer_transactions(cls):
            for transaction in cls.liste_transaction:
                  print(transaction)

      @staticmethod
      def aubaine():
            print("Épargner 50$ par mois vous donnera un montant de plus de 20 000$ dans 20 ans! ")
      @staticmethod
      def __temps_maintenant():
            return datetime.now().strftime("%H:%M:%S")

if __name__ == "__main__" :
      c1 = CompteBancaire("Steve", 20000)
      c1.deposer(100)
      #c1.retirer(100000000)
      c1.retirer(10000)
      c1.imprimer_transactions()
      c2 = CompteBancaire("Bobby",300)
      c2.deposer(105)
      CompteBancaire.imprimer_transactions()
