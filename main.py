import PhoneNumber as PN
import sys

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

line_number = 0
raw_number = ""  # Unnormalized

country_number_mapping = {"45": PN.DanishPhoneNumber(),
                          "46": PN.SwedishPhoneNumber(),
                          "47": PN.NorwegianPhoneNumber()}
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

        #check that phonenumber is a numeral and non-empty
        PN.PhoneNumber.normalized_number_error_check(number)

        # Find country code
        country = PN.PhoneNumber.identify_country(number)

        # Confirm that the number type is supported
        if country not in country_number_mapping.keys():
            raise ValueError("Unsupported country code")

        country_number_mapping[country].parse(number)

        # No exceptions raised. Number is correct
        number = country_number_mapping[country].format()
        output_file.write(number + "\n")

    # Phonenumber is wrong
    except TypeError as err:
        msg = "TypeError: {}\t{}: {}".format(err.message, str(line_number), raw_number)
        print msg
        err_log.write(msg)
        output_file.write(raw_number)

    except IndexError as err:
        msg = "IndexError: {}\t{}: {}".format(err.message, str(line_number), raw_number)
        print msg
        err_log.write(msg)
        output_file.write(raw_number)

    except ValueError as err:
        msg = "ValueError: {}\t{}: {}".format(err.message, str(line_number), raw_number)
        print msg
        err_log.write(msg)
        output_file.write(raw_number)

    line_number += 1