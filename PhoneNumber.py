from abc import ABCMeta, abstractmethod
import re
# Sjekk at nummer bare inneholder tall
# Sjekk at country code er med
# Sjekk at nummer har riktig lengde

class PhoneNumber(object):
    _country_code = ""
    _number = ""
    _raw_number = ""

    def __init__(self): pass

    # strip separators
    @staticmethod
    def normalize(number):
        # Strip number of all spaces
        number = re.sub("[\s\t\n]", "", number)

        # Make number completely numeric
        if len(number) > 0 and number[0] == "+":
            number = "00" + number[1:]  # Replace '+' with '00'

        # Remove all separation characters
        number = re.sub(r'\W+', '', number)

        return number

    @staticmethod
    def normalized_number_error_check(number):
        if not number:
            raise IndexError("Number is empty")
        elif not number.isdigit():
            raise ValueError("Number contains letters")

    @staticmethod
    def identify_country(number):
        if number[0:2] == "00":
            return number[2:4]
        elif number[0] == "+":
            return number[1:3]
        else:
            raise ValueError("No country code given")

    @abstractmethod
    def parse(self, number):
        self.number_length_check(number)
        self._number = number[4:]

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def number_length_check(self, number): pass
class DanishPhoneNumber(PhoneNumber):
    def __init__(self):
        super(PhoneNumber, self).__init__()
        self._country_code = "+45"

    def number_length_check(self, number):
        # Value checks
        super(PhoneNumber, self).__init__()

        # Length checks
        if len(number) < 12:
            raise IndexError("Number too short")
        if len(number) > 12:
            raise IndexError("Number too long")

    # Follows the format: "country code-number: 2-2-2-2"
    def format(self):
        number_str = self._number[:2] + " " + self._number[2:4] + " " + self._number[4:6] + " " + self._number[6:8]
        return self._country_code + " " + number_str
class SwedishPhoneNumber(PhoneNumber):
    _regional_code = ""

    def __init__(self):
        super(PhoneNumber, self).__init__()
        self._country_code = "+46"

    def number_length_check(self, number):
        # Value checks
        super(PhoneNumber, self).__init__()

        # Length checks
        if len(number) < 12:
            raise IndexError("Number too short")
        if len(number) > 16:
            raise IndexError("Number too long")

    def parse(self, number):
        self.number_length_check(number)

        self._number = number[-8:]          # Last eight digits
        self._regional_code = number[4:-8]  # Digits between the country code and the eight last

        # No regional code. Set to zero
        if not self._regional_code:
            self._regional_code = "0"

        # Zero pad the regional code until it is four digits long
        else:
            while len(self._regional_code) < 4:  # regional codes should be four digits long
                self._regional_code = "0" + self._regional_code

        self._regional_code = "(" + self._regional_code + ")"

    # Follows the format: "country code-regional code-number:"
    def format(self):
        number_str = self._country_code + " " + self._regional_code + " " + self._number
        return number_str
class NorwegianPhoneNumber(PhoneNumber):
    def __init__(self):
        super(PhoneNumber, self).__init__()
        self._country_code = "+47"

    def number_length_check(self, number):
        # Value checks
        super(PhoneNumber, self).__init__()

        # Length checks
        if len(number) < 12:
            raise IndexError("Number too short")
        if len(number) > 12:
            raise IndexError("Number too long")

    # Follows the format: "country code-number: 3-2-3"
    def format(self):
        number_str = self._number[:3] + " " + self._number[3:5] + " " + self._number[5:8]

        return self._country_code + " " + number_str