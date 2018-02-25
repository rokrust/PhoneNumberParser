1. File list
---------------
PhoneNumbers.py
main.py
test.py

2. Assumptions
---------------
 - All numbers must include a country code preceded by either '00' or '+'. 
 - Digits of the number can be separated by any number of non-alphanumeric characters. 
 - Numbers containing letters are considered faulty
 - Empty numbers are considered faulty

3. Program structure
---------------
In PhoneNumbers.py, a base class PhoneNumber is implemented with all country specific numbers inheriting from this. In main.py, the subclasses are mapped to their respective country codes through a dictionary. 
	    ---------Phonenumber---------
	   /		       |			\
	  /		       |			 \
	 /		       |			  \
	/		       |			   \
DanishPhoneNumber  SwedishPhoneNumber  NorwegianPhonenumber


main.py reads a list of numbers from a file one line at a time. Each number is first normalized by stripping any spaces or other separation characters, before the country code is identified and the appropriate class is instantiated. The eight end digits, and the regional code in the case of the Swedish numbers, are then parsed from the normalized number. Lastly, the extracted components are formatted before being written to the given output file.

The program runs a series of error checks during execution, raising an appropriate exception when a check fails. Any detected errors are reported in an error log, while the responsible number is written to the given output file as is.

The test program employs a series of unit tests based on the native python module "unittest".

4. Running the programs
---------------	
Formatting program
Input: 	Input file path, Output file path:
	(Numbers to be normalized, Normalized numbers output)
Output: List of normalized numbers, report with list of errors

The formatting program can be run by a python 2.7 compiler through the main.py file.
Example: python main.py phoneNumbers.txt normalizedPhoneNumbers.txt


test.py
Input:

The test program can be run by a python 2.7 compiler through the test.py file. Flags are included as desired, see the unittest python documentation.
Example: python test.py -V