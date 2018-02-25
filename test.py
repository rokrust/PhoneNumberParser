import PhoneNumber as PN
import unittest


class PhoneNumberTest(unittest.TestCase):
    def test_normalize(self):
        self.assertEqual(PN.PhoneNumber.normalize("+47 123 45678"), "004712345678")

    def test_country_identifier(self):
        self.assertEqual(PN.PhoneNumber.identify_country("+47 123 45678"), "47")

    def test

class DanishPhoneNumberTest(unittest.TestCase):
    def setUp(self):
        self.number = PN.DanishPhoneNumber("004512345678")

    def test_format(self):
        self.number.format()
        self.assertEqual(str(self.number), "+45 12 34 56 78")

class SwedishPhoneNumberTest(unittest.TestCase):
    def setUp(self):
        self.number_no_region = PN.SwedishPhoneNumber("004612345678")
        self.number_with_region = PN.SwedishPhoneNumber("004612312345678")

    def test_number_length_check_success(self):
        try:
            self.number_with_region.number_length_check("00461212345678")
        except:
            self.fail("Exception raised")

    def test_number_length_check_fail_too_short(self):
        with self.assertRaises(IndexError):
            self.number_with_region.number_length_check("0046123456")

    def test_number_length_check_fail_too_long(self):
        with self.assertRaises(IndexError):
            self.number_with_region.number_length_check("0046123456789012345")

    def test_parse(self):
        self.number_with_region.parse("004612312345678")
        self.number_no_region.parse("004612345678")

        self.assertEqual(self.number_with_region._regional_code, "(0123)")
        self.assertEqual(self.number_with_region._number, "12345678")

        self.assertEqual(self.number_no_region._number, "12345678")
        self.assertEqual(self.number_no_region._regional_code, "(0)")

    def test_format(self):
        self.number_with_region.format()
        self.number_no_region.format()

        self.assertEqual(str(self.number_no_region), "+46 (0) 12345678")
        self.assertEqual(str(self.number_with_region), "+46 (0123) 12345678")

class NorwegianPhoneNumberTest(unittest.TestCase):
    def setUp(self):
        self.number = PN.NorwegianPhoneNumber("004712345678")

    def test_number_init_fail_wrong_country_code(self):
        with self.assertRaises(ValueError):
            PN.NorwegianPhoneNumber("004512345678")

    def test_number_length_check_success(self):
        try:
            self.number.number_length_check("004712345678")
        except:
            self.fail("Exception raised")

    def test_number_length_check_fail_too_short(self):
        with self.assertRaises(IndexError):
            self.number.number_length_check("0047123")

    def test_number_length_check_fail_too_long(self):
        with self.assertRaises(IndexError):
            self.number.number_length_check("0047123456789012345")

    def test_parse(self):
        self.number.parse("004712345678")
        self.assertEqual(self.number._number, "12345678")

    def test_format(self):
        self.number.format()
        self.assertEqual(str(self.number), "+47 123 45 678")


if __name__ == "__main__":
    unittest.main()