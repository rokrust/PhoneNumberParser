from abc import ABCMeta, abstractmethod
import re

class PhoneNumber(object):
    country_code = ""
    _number = ""
    _formatted_number = ""

    def __init__(self, number):
        self.parse(number)
        self.format()

    def get_formatted_number(self):
        return self._formatted_number

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
    country_code = "45"
    def __init__(self, number):
        super(DanishPhoneNumber, self).__init__(number)

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
        number_str = "{} {} {} {}".format(self._number[:2], self._number[2:4], self._number[4:6], self._number[6:8])
        self._formatted_number = "+{} {}".format(self.country_code, number_str)
class SwedishPhoneNumber(PhoneNumber):
    country_code = "46"
    _regional_code = ""

    def __init__(self, number):
        super(SwedishPhoneNumber, self).__init__(number)

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
        self._formatted_number = "+{} {} {}".format(self.country_code, self._regional_code, self._number)
class NorwegianPhoneNumber(PhoneNumber):
    country_code = "47"

    def __init__(self, number):
        super(NorwegianPhoneNumber, self).__init__(number)

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
        number_str = "{} {} {}".format(self._number[:3], self._number[3:5], self._number[5:8])
        self._formatted_number = "+{} {}".format(self.country_code, number_str)