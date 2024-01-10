from sys import argv
from moteur_sans_variables.regle_sans_variables import RegleSansVariables
from moteur_sans_variables.connaissance import BaseConnaissances
from moteur_sans_variables.chainage_avant_sans_variables import ChainageAvantSansVariables

argv = [1, 'trace']
faits_initiaux = ['vin', '<-2-litres', '<-100-Euros', 'adulte']

# La description d'une règle est une liste de deux éléments:
# une liste de conditions, et une conclusion.
regles = [
          [['vin', '<-2-litres'], 'petite-quantité'],
          [['cognac', '<-1-litre'], 'petite-quantité'],
          [['<-100-Euros'], 'petite-quantité'],
          [['petite-quantité', 'adulte'], 'hors-taxe'],
        ]
        
bc = BaseConnaissances(lambda descr: RegleSansVariables(descr[0], descr[1]))
bc.ajoute_faits(faits_initiaux)
bc.ajoute_regles(regles)

moteur = ChainageAvantSansVariables(bc)
moteur.chaine()

moteur.affiche_solutions()

if len(argv) > 1 and argv[1].lower() == 'trace':
    # Utile durant le déboggage.
    moteur.affiche_trace()