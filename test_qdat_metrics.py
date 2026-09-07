import unittest

from qdat_metrics import etendue, mediane, moyenne, normaliser


class TestMoyenne(unittest.TestCase):
    def test_moyenne_simple(self):
        self.assertEqual(moyenne([2, 4, 6]), 4)

    def test_moyenne_negatifs(self):
        self.assertEqual(moyenne([-4, 4]), 0)

    def test_moyenne_liste_vide(self):
        with self.assertRaises(ValueError):
            moyenne([])


class TestMediane(unittest.TestCase):
    def test_mediane_impaire(self):
        self.assertEqual(mediane([9, 1, 5]), 5)

    def test_mediane_paire(self):
        self.assertEqual(mediane([1, 2, 3, 4]), 2.5)


class TestEtendue(unittest.TestCase):
    def test_etendue(self):
        self.assertEqual(etendue([3, 10, 7]), 7)


class TestNormaliser(unittest.TestCase):
    def test_normaliser_borne(self):
        self.assertEqual(normaliser([10, 20, 30]), [0.0, 0.5, 1.0])

    def test_normaliser_constante(self):
        self.assertEqual(normaliser([5, 5, 5]), [0.0, 0.0, 0.0])


if __name__ == "__main__":
    unittest.main()
