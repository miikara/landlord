import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_luodun_paatteen_saldo_oikein(self):
        balance = self.kassapaate.kassassa_rahaa
        self.assertEqual(balance, 100000)

    def test_luodun_paatteen_myynti_oikein(self):
        sales = self.kassapaate.edulliset + self.kassapaate.maukkaat
        self.assertEqual(sales, 0)

    def test_edullisen_myynti_kateisella_kasvattaa_myyntia(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_myynti_ei_kasvata_myyntia_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_myynti_kateisella_kasvattaa_kassaa(self):
        self.kassapaate.syo_edullisesti_kateisella(1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullisen_myynti_ei_kasvata_kassaa_kun_raha_ei_riita(self):
        self.kassapaate.syo_edullisesti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisen_myynti_kateisella_vaihtoraha_oikein(self):
        change = self.kassapaate.syo_edullisesti_kateisella(250)
        self.assertEqual(change, 10)
    
    def test_edullisen_myynti_kateisella_vaihtoraha_kun_raha_ei_riita(self):
        change = self.kassapaate.syo_edullisesti_kateisella(230)
        self.assertEqual(change, 230)

    def test_maukkaan_myynti_kateisella_kasvattaa_myyntia(self):
        self.kassapaate.syo_maukkaasti_kateisella(2000)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_myynti_ei_kasvata_myyntia_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_myynti_kateisella_kasvattaa_kassaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(2000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukkaan_myynti_ei_kasvata_kassaa_kun_raha_ei_riita(self):
        self.kassapaate.syo_maukkaasti_kateisella(10)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukkaan_myynti_kateisella_vaihtoraha_oikein(self):
        change = self.kassapaate.syo_maukkaasti_kateisella(410)
        self.assertEqual(change, 10)
    
    def test_maukkaan_myynti_kateisella_vaihtoraha_kun_raha_ei_riita(self):
        change = self.kassapaate.syo_maukkaasti_kateisella(230)
        self.assertEqual(change, 230)

    # Kortti edullinen

    def test_edullisen_myynti_kortilla_ei_muuta_kassaa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        balance = self.kassapaate.kassassa_rahaa
        self.assertEqual(balance, 100000)

    def test_edullisen_myynti_kortilla_kasvattaa_myyntia(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_myynti_kortilla_ei_kasvata_myyntia_kun_raha_ei_riita(self):
        maksukortti_low_balance = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti_low_balance)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullisen_myynti_kortilla_veloitetaan_kortilta(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 7.6")

    def test_edullisen_myynti_kortilla_ei_veloitusta_kun_raha_ei_riita(self):
        maksukortti_low_balance = Maksukortti(1)
        self.kassapaate.syo_edullisesti_kortilla(maksukortti_low_balance)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_edullisen_myynti_kortilla_palautusarvo(self):
        return_value = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(return_value, True)

    def test_edullisen_myynti_kortilla_palautusarvo_kun_raha_ei_riita(self):
        maksukortti_low_balance = Maksukortti(1)
        return_value = self.kassapaate.syo_edullisesti_kortilla(maksukortti_low_balance)
        self.assertEqual(return_value, False)

    # Kortti maukas

    def test_maukkaan_myynti_kortilla_ei_muuta_kassaa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        balance = self.kassapaate.kassassa_rahaa
        self.assertEqual(balance, 100000)
    
    def test_maukkaan_myynti_kortilla_kasvattaa_myyntia(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_myynti_kortilla_ei_kasvata_myyntia_kun_raha_ei_riita(self):
        maksukortti_low_balance = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti_low_balance)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_maukkaan_myynti_kortilla_veloitetaan_kortilta(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 6.0")

    def test_maukkaan_myynti_kortilla_ei_veloitusta_kun_raha_ei_riita(self):
        maksukortti_low_balance = Maksukortti(1)
        self.kassapaate.syo_maukkaasti_kortilla(maksukortti_low_balance)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_maukkaan_myynti_kortilla_palautusarvo(self):
        return_value = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(return_value, True)

    def test_maukkaan_myynti_kortilla_palautusarvo_kun_raha_ei_riita(self):
        maksukortti_low_balance = Maksukortti(1)
        return_value = self.kassapaate.syo_maukkaasti_kortilla(maksukortti_low_balance)
        self.assertEqual(return_value, False)

    # Lataus

    def test_kortin_lataus_kasvattaa_kassaa(self):
        maksukortti_temp = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti_temp, 1000)
        balance = self.kassapaate.kassassa_rahaa
        self.assertEqual(balance, 101000)

    def test_kortin_lataus_siirtyy_kortille(self):
        maksukortti_temp = Maksukortti(1000)
        self.kassapaate.lataa_rahaa_kortille(maksukortti_temp, 1000)
        self.assertEqual(str(maksukortti_temp), "saldo: 20.0")

    # Paluuarvo
    def test_negatiivinen_lataus_kortille(self):
        maksukortti_temp = Maksukortti(1000)
        return_value = self.kassapaate.lataa_rahaa_kortille(maksukortti_temp, -500)
        self.assertEqual(str(maksukortti_temp), "saldo: 10.0")



