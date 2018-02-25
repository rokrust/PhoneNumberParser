import PhoneNumber as PN

number_str = "004712345678"
number_str = PN.PhoneNumber.normalize(number_str)
print "Normalize: " + number_str

number_inst = PN.NorwegianPhoneNumber(number_str)
print "Identify_country: " + PN.PhoneNumber.identify_country(number_str)

number_inst.parse(number_str)
print "Parse: " + number_inst.country_code + number_inst._number

number_inst.format()
print "Format: " + str(number_inst)