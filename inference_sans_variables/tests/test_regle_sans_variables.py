from unittest import TestCase
from moteur_sans_variables.regle_sans_variables import RegleSansVariables

class TestRegle(TestCase):

    def setUp(self):
        self.regle = RegleSansVariables(['fait1', 'fait2'], 'conclusion')

    def test_depend_de(self):
        self.assertTrue(self.regle.depend_de('fait1'))
        self.assertFalse(self.regle.depend_de('fait234'))

    def test_satisfaite_par(self):
        self.assertTrue(self.regle.satisfaite_par(['fait1', 'fait2']))
        self.assertFalse(self.regle.satisfaite_par(['fait1', 'fait3']))