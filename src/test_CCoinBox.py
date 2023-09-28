import unittest
from CCoinBox import CCoinBox

class Test_CCoinBox(unittest.TestCase):
    def setUp(self):
        self.box = CCoinBox()

    def test_ajouter_25c(self):
        self.box.ajouter_25c()
        self.assertEqual(self.box.monnaie_courante, 1)

    def test_vente(self):
        self.box.ajouter_25c()
        self.box.vente()
        self.assertEqual(self.box.monnaie_totale, 0)
