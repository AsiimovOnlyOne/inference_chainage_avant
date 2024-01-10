from unittest import TestCase
from moteur_sans_variables.regle_sans_variables import RegleSansVariables
from moteur_sans_variables.connaissance import BaseConnaissances
from moteur_sans_variables.chainage_avant_sans_variables import ChainageAvantSansVariables

class TestChainageAvant(TestCase):

    def test_chainage(self):
        faits = ['vin', '<-2-litres', '<-100-Euro', 'adulte']
        regles = [
                  [['vin', '<-2-litres'], 'petite-quantité'],
                  [['cognac', '<-1-litre'], 'petite-quantité'],
                  [['<-100-Euro'], 'petite-quantité'],
                  [['petite-quantité', 'adulte'], 'hors-taxe'],
                 ]

        bc = BaseConnaissances(lambda d: RegleSansVariables(d[0], d[1]))
        bc.ajoute_faits(faits)
        bc.ajoute_regles(regles)

        moteur = ChainageAvantSansVariables(bc)
        solutions = moteur.chaine()
        
        but = 'hors-taxe'
        self.assertTrue(but in solutions)

    def test_pas_de_propositions(self):
        faits = []
        regles = [
                  [['vin', '<-2-litres'], 'petite-quantité'],
                  [['cognac', '<-1-litre'], 'petite-quantité'],
                  [['<-100-Euro'], 'petite-quantité'],
                ]

        bc = BaseConnaissances(lambda d: RegleSansVariables(d[0], d[1]))
        bc.ajoute_faits(faits)
        bc.ajoute_regles(regles)

        moteur = ChainageAvantSansVariables(bc)
        solutions = moteur.chaine()

        self.assertEqual([], solutions)

    def test_propositions_redondantes(self):
        faits = ['vin', 'vin', '<-2-litres', '<-100-Euro', 'adulte']
        regles = [
                  [['vin', '<-2-litres'], 'petite-quantité'],
                  [['cognac', '<-1-litre'], 'petite-quantité'],
                  [['<-100-Euro'], 'petite-quantité'],
                  [['petite-quantité', 'adulte'], 'hors-taxe'],
                ]

        bc = BaseConnaissances(lambda d: RegleSansVariables(d[0], d[1]))
        bc.ajoute_faits(faits)
        bc.ajoute_regles(regles)

        moteur = ChainageAvantSansVariables(bc)
        solutions = moteur.chaine()

        but = 'hors-taxe'
        self.assertTrue(but in solutions)