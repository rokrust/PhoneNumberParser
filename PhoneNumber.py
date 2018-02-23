from abc import ABCMeta, abstractmethod
import exceptions
# Sjekk at nummer bare inneholder tall
# Sjekk at country code er med
# Sjekk at nummer har riktig lengde

class PhoneNumber(object):
    _country_code = ""
    _number = ""

    def __init__(self): pass

    # strip chars
    @staticmethod
    def normalize(number):
        number.rstrip()                 # Remove newline character
        number.replace(" ", "")         # Remove all whitespace characters
        number.replace("\t", "")        # Remove all tabular characters

        if not number:
            raise IndexError("Number is empty")

        if number[0] == "+":
            number = "00" + number[1:]  # Replace '+' with '00'

        # Remove all separation characters
        i = 0
        while i < len(number):
            if not number[i].isalnum():
                number = number[:i] + number[i + 1:]  # Remove character from number
                i -= 1                                # length of string decreased

            i += 1

        return number

    @staticmethod
    def identify_country(number):
        if number[0:2] == "00":
            return number[2:4]
        elif number[0] == "+":
            return number[1:3]
        else:
            raise ValueError("No country code given")

    @abstractmethod
    def parse(self, number): pass

    @abstractmethod
    def format(self): pass

    @abstractmethod
    def error_check(self, number):
        # Value checks
        if not number.isdigit():
            raise ValueError("Number contains non-numerals")
        elif not number:
            raise ValueError("Number is empty")

        # Length checks
        if len(number) < 12:
            raise IndexError("Number too short")
        if len(number) > 12:
            raise IndexError("Number too long")

class DanishPhoneNumber(PhoneNumber):
    def __init__(self):
        super(PhoneNumber, self).__init__()
        self._country_code = "+45"

    def parse(self, number):
        self.error_check(number)
        self._number = number[4:]

    # Follows the format: "country code-number: 2-2-2-2"
    def format(self):
        # Put two digits together, seperate by space
        number_str = self._number[:2] + " " + self._number[2:4] + " " + self._number[4:6] + " " + self._number[6:8]
        return self._country_code + " " + number_str
class SwedishPhoneNumber(PhoneNumber):
    _regional_code = ""

    def __init__(self):
        super(PhoneNumber, self).__init__()
        self._country_code = "+46"

    def error_check(self, number):
        # Value checks
        if not number.isdigit():
            raise ValueError("Number contains non-numerals")
        elif not number:
            raise ValueError("Number is empty")

        # Length checks
        if len(number) < 12:
            raise IndexError("Number too short")
        if len(number) > 16:
            raise IndexError("Number too long")

    def parse(self, number):
        self.error_check(number)

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

    def parse(self, number):
        self.error_check(number)
        self._number = number[4:]

    # Follows the format: "country code-number: 3-2-3"
    def format(self):
        number_str = self._number[:3] + " " + self._number[3:5] + " " + self._number[5:8]

        return self._country_code + " " + number_str