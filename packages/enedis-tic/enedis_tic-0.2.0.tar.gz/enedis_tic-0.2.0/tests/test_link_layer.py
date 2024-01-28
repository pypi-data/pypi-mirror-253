from unittest import TestCase
from datetime import datetime

from enedis_tic.link_layer import SumChecker, InvalidDatasetError, FrameFactory, InvalidChecksumError


START_FRAME = b'\x02'.decode('ascii')
END_FRAME = b'\x03'.decode('ascii')


def frame(raw):
    return FrameFactory(raw).to_dict()


def data_set(raw, sep='\t'):
    return FrameFactory.data_set(raw, sep)


class FrameTest(TestCase):
    def test_no_dataset(self):
        with self.assertRaises(RuntimeError) as cm:
            frame(START_FRAME + END_FRAME)
        self.assertEqual('Empty Frame', cm.exception.args[0])

    def test_minimal(self):
        actual = frame(START_FRAME + '\nLABEL\tDATA\t#\r' + END_FRAME)
        expected = {'LABEL': 'DATA'}
        self.assertEqual(expected, actual)

    def test_many_data_set(self):
        actual = frame(START_FRAME + '\nLABEL\tDATA\t#\r\nLABEL2\tDATA2\tP\r' + END_FRAME)
        expected = {'LABEL': 'DATA', 'LABEL2': 'DATA2'}
        self.assertEqual(expected, actual)


class DataSetTest(TestCase):
    def test_valid_historique(self):
        actual = data_set('LABEL\tDATA\t#')
        expected = {'label': 'LABEL', 'data': 'DATA'}
        self.assertEqual(expected, actual)

    def test_valid_historique_older(self):
        actual = data_set('LABEL DATA :', sep=' ')
        expected = {'label': 'LABEL', 'data': 'DATA'}
        self.assertEqual(expected, actual)

    def test_valid_standard(self):
        actual = data_set('LABEL\tH081225223518\tDATA\t$')
        expected = {'label': 'LABEL', 'data': 'DATA', 'datetime': datetime(2008, 12, 25, 22, 35, 18)}
        self.assertEqual(expected, actual)

    def test_invalid_checksum(self):
        raw = 'LABEL DATA f'
        with self.assertRaises(InvalidChecksumError) as cm:
            data_set(raw, sep=' ')
        self.assertEqual(raw, cm.exception.raw_dataset)

    def test_no_data(self):
        raw_frame = ''
        with self.assertRaises(InvalidDatasetError) as cm:
            data_set(raw_frame)
        self.assertEqual(raw_frame, cm.exception.raw_frame)

    def test_only_label(self):
        raw_frame = 'aA'
        with self.assertRaises(InvalidDatasetError) as cm:
            data_set(raw_frame)
        self.assertEqual(raw_frame, cm.exception.raw_frame)


class ChecksumTest(TestCase):
    def test_verify_sp_older(self):
        self.assertTrue(SumChecker('LABEL DATA :').verify())

    def test_verify_sp_newer(self):
        self.assertTrue(SumChecker('LABEL DATA Z').verify())

    def test_verify_ht_older(self):
        self.assertTrue(SumChecker('LABEL\tDATA\t#').verify())

    def test_verify_ht_newer(self):
        self.assertTrue(SumChecker('LABEL\tDATA\t,').verify())

    def test_verify_datetime(self):
        self.assertTrue(SumChecker('LABEL\tH081225223518\tDATA\t$').verify())

    def test_verify_fail(self):
        self.assertFalse(SumChecker('LABEL DATA f').verify())

    def test_verify_invalid_data_set(self):
        """The given data_set is invalid, but we don't care of its validity at that level."""
        self.assertTrue(SumChecker('aA').verify())
