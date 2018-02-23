import PhoneNumber as PN
import sys

try:
    if len(sys.argv) < 3:
        raise TypeError("Not enough input arguments")
    elif len(sys.argv) > 3:
        raise TypeError("Too many input arguments")
except TypeError as err:
    print err

in_file = sys.argv[1]
out_file = sys.argv[2]

line_number = 0
raw_number = ""  # Unnormalized

phone_number = {"45": PN.DanishPhoneNumber(),
                "46": PN.SwedishPhoneNumber(),
                "47": PN.NorwegianPhoneNumber()}
input_file = open(in_file, "r")
output_file = open(out_file, "w")

# With statement is exited early when using exceptions
while True:
    raw_number = input_file.readline()
    if not raw_number:
        break

    try:
        number = PN.PhoneNumber.normalize(raw_number)
        country = PN.PhoneNumber.identify_country(number)
        phone_number[country].parse(number)  # Accepts normalized numbers only

        # No exceptions raised. Number is correct
        number = phone_number[country].format()
        output_file.write(number + "\n")

        line_number += 1


    except TypeError as err:
        msg = "TypeError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
        output_file.write(raw_number)
    except IndexError as err:
        msg = "IndexError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
    except ValueError as err:
        msg = "ValueError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
        output_file.write(raw_number)