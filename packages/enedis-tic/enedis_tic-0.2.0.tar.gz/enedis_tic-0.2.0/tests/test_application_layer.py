from unittest import TestCase

from enedis_tic.application_layer import FrameParser


def parse_frame(raw):
    return FrameParser(raw).to_dict()


class AdcoTest(TestCase):
    def test_adco(self):
        expected = {
            "Adresse du compteur": "123456789ABC"
        }
        actual = parse_frame({'ADCO': '123456789ABC'})
        self.assertEqual(expected, actual)


class AdscTest(TestCase):

    def test_adsc(self):
        expected = {
            "Adresse secondaire du compteur": "841961789ABC",
            "Constructeur": "SAGEM / SAGEMCOM",
            "Appareil": "Compteur monophasé 60A LINKY - généralisation G3 - arrivée haute",
            "Année de fabrication": 2019,
            "Numéro de série": "789ABC"
        }
        actual = parse_frame({'ADSC': '841961789ABC'})
        self.assertEqual(expected, actual)

    def test_constructeur_none(self):
        actual = parse_frame({'ADSC': 'XX6119789ABC'})
        self.assertIsNone(actual['Constructeur'])

    def test_appareil_none(self):
        actual = parse_frame({'ADSC': '8419XX789ABC'})
        self.assertIsNone(actual['Appareil'])

    def test_invalid_year(self):
        actual = parse_frame({'ADSC': '84XX61789ABC'})
        self.assertIsNone(actual.get('Année de fabrication'))


class OptarifTest(TestCase):
    def test_base(self):
        self.assertEqual({'Option tarifaire choisie': 'Base'}, parse_frame({'OPTARIF': 'BASE'}))

    def test_hc(self):
        self.assertEqual({'Option tarifaire choisie': 'Heures Creuses'}, parse_frame({'OPTARIF': 'HC..'}))

    def test_tempo(self):
        self.assertEqual({'Option tarifaire choisie': 'Tempo'}, parse_frame({'OPTARIF': 'BBR.'}))

    def test_ejp(self):
        self.assertEqual({'Option tarifaire choisie': 'EJP'}, parse_frame({'OPTARIF': 'EJP.'}))


class IsouscTest(TestCase):
    def test_isousc(self):
        actual = parse_frame({'ISOUSC': '12'})
        self.assertTrue('Intensité souscrite' in actual)
        self.assertEqual(12, actual['Intensité souscrite'].value)
        self.assertEqual('A', actual['Intensité souscrite'].unit)

