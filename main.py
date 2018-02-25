import PhoneNumber as PN
import sys

def exception_handler(err, line_number, raw_number):
    msg = "{}\t at line {}: {}".format(err.message, str(line_number), raw_number)
    print msg
    err_log.write(msg)
    output_file.write(raw_number)

try:
    if len(sys.argv) < 3:
        raise TypeError("Not enough input arguments")
    elif len(sys.argv) > 3:
        raise TypeError("Too many input arguments")
except TypeError as err:
    print err
    exit(1)

in_file = sys.argv[1]
out_file = sys.argv[2]

line_number = 1
raw_number = ""  # Unnormalized

country_number_mapping = {
    PN.DanishPhoneNumber.country_code: PN.DanishPhoneNumber,
    PN.SwedishPhoneNumber.country_code: PN.SwedishPhoneNumber,
    PN.NorwegianPhoneNumber.country_code: PN.NorwegianPhoneNumber
}

input_file = open(in_file, "r")
output_file = open(out_file, "w")
err_log = open("error_log.txt", "w")

# With statement is exited early when using exceptions
while True:
    raw_number = input_file.readline()

    # End of input_file
    if not raw_number:
        input_file.close()
        output_file.close()
        break

    try:
        # Strip phonenumber of spaces and non-alphanumeric separation characters
        number = PN.PhoneNumber.normalize(raw_number)

        #Confirm that phonenumber is numeral and non-empty
        PN.PhoneNumber.normalized_number_error_check(number)

        # Find country code
        country = PN.PhoneNumber.identify_country(number)

        # Confirm that the number type is supported
        if country not in country_number_mapping.keys():
            raise ValueError("ValueError: Unsupported country code")

        # Instantiate appropriate class according to country code
        number_instance = country_number_mapping[country](number)

        # Formatting successful. No exceptions raised
        number = number_instance.get_formatted_number()
        output_file.write(number + "\n")

    # Formatting unsuccessful.
    except TypeError as err:
        exception_handler(err, line_number, raw_number)

    except IndexError as err:
        exception_handler(err, line_number, raw_number)

    except ValueError as err:
        exception_handler(err, line_number, raw_number)

    line_number += 1
