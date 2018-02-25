import PhoneNumber as PN
import unittest

class DanishPhoneNumberTest(unittest.TestCase):
    def setUp(self):
        self.raw_number = "0045 123   4567 8"
        self.expected_normalized_number = "004512345678"
        self.expected_country_code = "45"
        self.expected_formatted_number = "+45 12 34 56 78"

        self.number = PN.DanishPhoneNumber(self.expected_normalized_number)

    def test_normalize(self):
        self.assertEqual(PN.PhoneNumber.normalize(self.raw_number), self.expected_normalized_number)

    def test_country_identifier(self):
        self.assertEqual(PN.PhoneNumber.identify_country(self.expected_normalized_number), self.expected_country_code)

    def test_format(self):
        self.number.format()
        self.assertEqual(str(self.number), self.expected_formatted_number)

class SwedishPhoneNumberTest(unittest.TestCase):
    def setUp(self):
        self.raw_number = "0046 123 12345678"
        self.expected_normalized_number = "004612312345678"
        self.expected_country_code = "46"
        self.expected_formatted_number = "+46 (0123) 12345678"
        self.number = PN.SwedishPhoneNumber(self.expected_normalized_number)

    def test_normalize(self):
        self.assertEqual(PN.PhoneNumber.normalize(self.raw_number), self.expected_normalized_number)

    def test_country_identifier(self):
        self.assertEqual(PN.PhoneNumber.identify_country(self.expected_normalized_number), self.expected_country_code)

    def test_format(self):
        self.number.format()
        self.assertEqual(str(self.number), self.expected_formatted_number)

class NorewegianPhoneNumberTest(unittest.TestCase):
    def setUp(self):
        self.raw_number = "0047 123   4567 8"
        self.expected_normalized_number = "004712345678"
        self.expected_country_code = "47"
        self.expected_formatted_number = "+47 123 45 678"

        self.normalized_number = PN.PhoneNumber.normalize(self.raw_number)
        self.number = PN.NorwegianPhoneNumber(self.expected_normalized_number)

    def test_normalize(self):
        self.assertEqual(PN.PhoneNumber.normalize(self.raw_number), self.expected_normalized_number)

    def test_country_identifier(self):
        self.assertEqual(PN.PhoneNumber.identify_country(self.expected_normalized_number), self.expected_country_code)

    def test_format(self):
        self.number.format()
        self.assertEqual(str(self.number), self.expected_formatted_number)


if __name__ == "__main__":
    unittest.main()