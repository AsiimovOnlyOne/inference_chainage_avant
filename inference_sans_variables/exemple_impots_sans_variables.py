from sys import argv, exit
from moteur_sans_variables.regle_sans_variables import RegleSansVariables
from moteur_sans_variables.connaissance import BaseConnaissances
from moteur_sans_variables.chainage_avant_sans_variables import ChainageAvantSansVariables

# La description d'une règle est une liste de deux éléments:
# une liste de conditions, et une conclusion.
regles = [
          [['pas-d-enfants'], 'réduc-enfant-0'],
          [['enfants'], 'réduc-enfant-100'],
          [['bas-salaire'], 'réduc-loyer-200'],
          [['moyen-salaire'], 'réduc-loyer-100'],
          [['haut-salaire'], 'réduc-loyer-0'],
          [['pas-de-loyer'], 'réduc-loyer-0'],
          [['petit-trajet'], 'réduc-trajet-0'],
          [['réduc-enfant-0', 'long-trajet'], 'réduc-trajet-100'],
          [['réduc-loyer-0', 'long-trajet'], 'réduc-trajet-100'],
          [['réduc-enfant-100', 'réduc-loyer-100', 'long-trajet'], 
           'réduc-trajet-50'],
          [['réduc-enfant-100', 'réduc-loyer-200', 'long-trajet'], 
           'réduc-trajet-0'],
          [['réduc-enfant-0', 'réduc-loyer-0', 'réduc-trajet-0'], 
           'réduc-0'],
          [['réduc-enfant-100', 'réduc-loyer-0', 'réduc-trajet-0'], 
           'réduc-100'],
          [['réduc-enfant-0', 'réduc-loyer-100', 'réduc-trajet-0'], 
           'réduc-100'],
          [['réduc-enfant-100', 'réduc-loyer-100', 'réduc-trajet-0'], 
           'réduc-200'],
          [['réduc-enfant-0', 'réduc-loyer-200', 'réduc-trajet-0'], 
           'réduc-200'],
          [['réduc-enfant-100', 'réduc-loyer-200', 'réduc-trajet-0'], 
           'réduc-300'],
          [['réduc-enfant-0', 'réduc-loyer-0', 'réduc-trajet-50'], 
           'réduc-50'],
          [['réduc-enfant-100', 'réduc-loyer-0', 'réduc-trajet-50'], 
           'réduc-150'],
          [['réduc-enfant-0', 'réduc-loyer-100', 'réduc-trajet-50'], 
           'réduc-150'],
          [['réduc-enfant-100', 'réduc-loyer-100', 'réduc-trajet-50'], 
           'réduc-250'],
          [['réduc-enfant-0', 'réduc-loyer-200', 'réduc-trajet-50'], 
           'réduc-250'],
          [['réduc-enfant-0', 'réduc-loyer-200', 'réduc-trajet-50'], 
           'réduc-250'],
          [['réduc-enfant-100', 'réduc-loyer-200', 'réduc-trajet-50'], 
           'réduc-350'],
          [['réduc-enfant-0', 'réduc-loyer-0', 'réduc-trajet-100'], 
           'réduc-100'],
          [['réduc-enfant-100', 'réduc-loyer-0', 'réduc-trajet-100'], 
           'réduc-200'],
          [['réduc-enfant-0', 'réduc-loyer-100', 'réduc-trajet-100'], 
           'réduc-200'],
          [['réduc-enfant-100', 'réduc-loyer-100', 'réduc-trajet-100'], 
           'réduc-300'],
          [['réduc-enfant-0', 'réduc-loyer-200', 'réduc-trajet-100'], 
           'réduc-300'],
          [['réduc-enfant-100', 'réduc-loyer-200', 'réduc-trajet-100'], 
           'réduc-400'],
        ]

argv = [1,'a','trace']

if len(argv) < 2 or argv[1].lower() not in ('a', 'b'):
    print('On attend au moins un arguments: A ou B')
    exit(1)

if argv[1].lower() == 'a':
    faits_initiaux = ['bas-salaire', 'loyer', 'enfants', 'long-trajet']
elif argv[1].lower() == 'b':
    faits_initiaux = ['pas-d-enfants', 'pas-de-loyer',
                      'haut-salaire', 'long-trajet']

bc = BaseConnaissances(lambda descr: RegleSansVariables(descr[0], descr[1]))
bc.ajoute_faits(faits_initiaux)
bc.ajoute_regles(regles)

moteur = ChainageAvantSansVariables(bc)
moteur.chaine()

moteur.affiche_solutions()

if len(argv) > 2 and argv[2].lower() == 'trace':
    # Utile durant le déboggage.
    moteur.affiche_trace()