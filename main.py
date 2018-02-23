import PhoneNumber as PN
import sys

err_list = []
# Make sure that two arguments, input and output file name, has been supplied
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
with open(in_file, "rb") as input_file:#, \
     #open(out_file, "wb") as output_file:#, \
     #open("error_log.txt", "w") as err_log:
    phone_number = { "45": PN.DanishPhoneNumber(),
                     "46": PN.SwedishPhoneNumber(),
                     "47": PN.NorwegianPhoneNumber() }

    try:
        raw_number = input_file.readline()
        number = PN.PhoneNumber.normalize(raw_number)
        country = PN.PhoneNumber.identify_country(number)
        phone_number[country].parse(number)                    # Accepts normalized numbers only

        # No exceptions raised. Number is correct
        number = phone_number[country].format()
        #output_file.write(number + "\n")

        line_number += 1

    except TypeError as err:
        msg = "TypeError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
 #       err_log.write(msg)
    except IndexError as err:
        msg = "IndexError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
 #       err_log.write(msg)
    except ValueError as err:
        msg = "ValueError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
 #       err_log.write(msg)

#output_file.close()

#with open(in_file, "rb") as input_file:  # , \
    # open(out_file, "wb") as output_file:#, \
    # open("error_log.txt", "w") as err_log:
phone_number = {"45": PN.DanishPhoneNumber(),
                "46": PN.SwedishPhoneNumber(),
                "47": PN.NorwegianPhoneNumber()}
input_file = open(in_file, "r")
output_file = open(out_file, "w")
while True:
    try:
        raw_number = input_file.readline()
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
        input_file.close()
        output_file.close()
        break
#        err_log.write(msg)
    except ValueError as err:
        msg = "ValueError: " + err.message + "\t" + str(line_number) + ": " + raw_number + "\n"
        print msg
#        err_log.write(msg)
        output_file.write(raw_number)
