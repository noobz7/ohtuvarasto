"""testejä """
import unittest
from varasto import Varasto

class TestVarasto(unittest.TestCase):
    """luokka tekee testit varastolle"""
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """testi"""
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """testi"""
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """testi"""
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """testi"""
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """testi"""
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """testi"""
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_varastoon_liikaa_tavaraa(self):
        """testi"""
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_alku_tilavuus(self):
        """testi"""
        self.varasto = Varasto(-1)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_alku_saldo(self):
        """testi"""
        self.varasto = Varasto(10, -3)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_lisataan_alle_nolla(self):
        """testi"""
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_otetaan_varastosta_alle_nolla(self):
        """testi"""
        self.varasto.ota_varastosta(-2)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_varastosta_otetaan_kaikki(self):
        """testi"""
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(4)
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_str(self):
        """testi"""
        self.assertAlmostEqual(str(self.varasto), "saldo = 0, vielä tilaa 10")
