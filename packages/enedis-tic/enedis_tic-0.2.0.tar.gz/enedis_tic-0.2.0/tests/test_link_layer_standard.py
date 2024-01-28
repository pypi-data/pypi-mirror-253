from unittest import TestCase
from datetime import datetime

from enedis_tic.link_layer import FrameFactory


def data_set(raw, sep='\t'):
    return FrameFactory.data_set(raw, sep)


class DataSetTest(TestCase):
    def test_without_horodate(self):
        actual = data_set('VTIC\t02\tJ')
        expected = {'label': 'VTIC', 'data': '02'}
        self.assertEqual(expected, actual)

    def test_horodate_without_data(self):
        actual = data_set('DATE\tH240107121638\t\tD')
        expected = {'label': 'DATE', 'data': '', 'datetime': datetime(year=2024, month=1, day=7, hour=12, minute=16, second=38)}
        self.assertEqual(expected, actual)

    def test_with_horodatage(self):
        actual = data_set('SMAXSN\tH240107111839\t01610\t:')
        expected = {'label': 'SMAXSN', 'data': '01610', 'datetime': datetime(year=2024, month=1, day=7, hour=11, minute=18, second=39)}
        self.assertEqual(expected, actual)