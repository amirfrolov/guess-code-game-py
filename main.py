import os
from os.path import abspath #for opening files
os.chdir(os.path.dirname(__file__)) #set the path for opening files
from collections import deque, Counter
import random

CODE_SIZE = 4
INSTRUCTIONS_FILE = "instructions.txt"

#colors - https://www.geeksforgeeks.org/print-colors-python-terminal/
class bcolors:
    red='\033[31m'
    yellow='\033[93m'
    purple='\033[35m'
    lightblue='\033[94m'
    green='\033[32m'
    ENDC = '\033[0m'
    BOLDget_secret_code = '\033[1m'
    UNDERLINE = '\033[4m'

#returns a random secret code
def get_secret_code():
    result = deque()
    digits = deque([i for i in range(10)])
    for i in range(CODE_SIZE):
        digit_index = random.randint(0,9 - i)
        result.append(digits[digit_index])
        del digits[digit_index]
    return [str(i) for i in result]

#checks if all the characters in the string are present only once.
def is_unique_chars(string):
	# Counting frequency
	freq = Counter(string)

	if(len(freq) == len(string)):
		return True
	else:
		return False

#get a code guess from the user, if user guess invalid try again
def get_code_guess():
    error_flag = True
    while error_flag:
        error_flag = False
        code_guess = input("Enter a guess (Example: 1234):")
        #check errors
        if len(code_guess) != CODE_SIZE:
            error_flag = True
            print("Guess length is not 4 digits, Try again.")
        elif not code_guess.isdigit():
            error_flag = True
            print("Guess does not contain only digits, Try again.")
        elif not is_unique_chars(code_guess):
            error_flag = True
            print("Guess does not contain only unique digits, Try again.")
    return code_guess

#   ----------Main----------
def main():
    secret_code =  get_secret_code()
    win = False
    attempts = 0
    #print instructions
    with open(abspath(INSTRUCTIONS_FILE), 'r') as file_handle:
        print(file_handle.read())
    #main code
    while not win:
        attempts += 1
        print(f"Attempt {attempts}: ", end="")
        code_guess = get_code_guess()
        #change print color
        print(end=bcolors.green)
        print(code_guess)
        digit_exists_counter = 0
        same_place_counter = 0
        for i in range(CODE_SIZE):
            #if the digit is in the right place
            if secret_code[i] == code_guess[i]:
                same_place_counter += 1
            #if the digit is not in the right place exists
            elif secret_code[i] in code_guess:
                digit_exists_counter += 1
        
        if same_place_counter == CODE_SIZE:
            win = True
            print(f"You won! After {attempts} attempts.")
        else:
            print(f"Direct hits:     {same_place_counter}")
            print(f"Not direct hits: {digit_exists_counter}")
        #restore print color
        print(end=bcolors.ENDC)
    return None
#   ----------End-----------

if __name__ == "__main__":
    print("ctrl+c to exit the proggram")
    try:
        main()
    except KeyboardInterrupt:
        print(" -proggram sttoped")