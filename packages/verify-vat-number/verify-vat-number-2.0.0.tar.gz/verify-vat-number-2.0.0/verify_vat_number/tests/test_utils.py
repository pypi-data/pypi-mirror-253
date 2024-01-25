from datetime import date
from unittest import TestCase

from freezegun import freeze_time

from verify_vat_number.utils import (is_deletion_date, join_by_separator, make_lower_with_capital, only_str, parse_date,
                                     strip_vat_id_number, strip_vat_reg_number, value_to_str)


class TestUtils(TestCase):

    ascii = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\t\r\n'

    def test_strip_vat_id_number(self):
        self.assertEqual(strip_vat_id_number(self.ascii), '0123456789')

    def test_strip_vat_reg_number(self):
        code = strip_vat_reg_number(self.ascii)
        self.assertEqual(code, '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')

    def test_join_by_separator_no_data(self):
        self.assertIsNone(join_by_separator(', ', []))

    def test_join_by_separator(self):
        self.assertEqual(join_by_separator(', ', ['a', None, 1, None, 'b']), 'a, 1, b')

    def test_parse_date_none(self):
        self.assertIsNone(parse_date(None))

    def test_parse_date(self):
        self.assertEqual(parse_date('2024-01-05'), date(2024, 1, 5))

    def test_is_deletion_date_none(self):
        self.assertFalse(is_deletion_date(None))

    @freeze_time("2024-01-04")
    def test_is_deletion_date_in_past(self):
        self.assertTrue(is_deletion_date('2024-01-03'))

    @freeze_time("2024-01-04")
    def test_is_deletion_date_equal(self):
        self.assertTrue(is_deletion_date('2024-01-04'))

    @freeze_time("2024-01-04")
    def test_is_deletion_date_in_future(self):
        self.assertFalse(is_deletion_date('2024-01-05'))

    def test_value_to_str_none(self):
        self.assertEqual(value_to_str(None), "")

    def test_value_to_str_str(self):
        self.assertEqual(value_to_str("OK"), "OK")

    def test_value_to_str_int(self):
        self.assertEqual(value_to_str(42), "42")

    def test_make_lower_with_capital_none(self):
        self.assertIsNone(make_lower_with_capital(None))

    def test_make_lower_with_capital(self):
        self.assertEqual(make_lower_with_capital("ARNOLD RIMMER"), 'Arnold Rimmer')

    def test_make_lower_exceptions(self):
        source = "D'ARTAGNAN, D’ARTAGNAN, D‘ARTAGNAN CHARLES DE BATZ-CASTELMORE"
        destin = "d'Artagnan, d’Artagnan, d‘Artagnan Charles de Batz-Castelmore"
        self.assertEqual(make_lower_with_capital(source), destin)

    def test_only_str_none(self):
        self.assertIsNone(only_str(None))

    def test_only_str_str(self):
        self.assertEqual(only_str("42"), "42")

    def test_only_str_int(self):
        self.assertEqual(only_str(42), "42")
