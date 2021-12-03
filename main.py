from collections import deque, Counter
import random

CODE_SIZE = 4
INSTRUCTIONS = """
Enter a 4 digit number to guess the secret code.
The code is made of 4 diffrent digits from 0-9.
After every attempt you will get the number of digits
you found are in the right place in the secret code (direct hits)
And the number of digits you found are in the secret code
but not in the right place (not direct hits).
the goal is to guess the secret code.
good luck!
"""

#colors - https://www.geeksforgeeks.org/print-colors-python-terminal/
class bcolors:
    red='\033[31m'
    yellow='\033[93m'
    purple='\033[35m'
    lightblue='\033[94m'
    green='\033[32m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
def get_secret_code():
    result = deque()
    digits = deque([i for i in range(10)])
    for i in range(CODE_SIZE):
        digit_index = random.randint(0,9 - i)
        result.append(digits[digit_index])
        del digits[digit_index]
    return [str(i) for i in result]

def is_unique_chars(string):
	# Counting frequency
	freq = Counter(string)

	if(len(freq) == len(string)):
		return True
	else:
		return False

def get_code_guess():
    error_flag = True
    while error_flag:
        error_flag = False
        code_guess = input("Enter a guess (Example: 1234):")
        #check errors
        if len(code_guess) != CODE_SIZE:
            error_flag = True
            print("Guess length is not 4 digits, Try again.")
        if not error_flag and not code_guess.isdigit():
            error_flag = True
            print("Guess does not contain only digits, Try again.")
        if not error_flag and not is_unique_chars(code_guess):
            error_flag = True
            print("Guess does not contain only unique digits, Try again.")
    return code_guess

#   ----------Main----------
def main():
    print(INSTRUCTIONS)
    secret_code =  get_secret_code()
    win = False
    attempts = 0
    while not win:
        attempts += 1
        print(f"Attempt {attempts}: ", end="")
        code_guess = get_code_guess()
        #change print color
        print(end=bcolors.green)
        print(code_guess)
        same_digits = 0
        same_place = 0
        for i in range(CODE_SIZE):
            if secret_code[i] == code_guess[i]:
                same_place += 1
            elif secret_code[i] in code_guess:
                same_digits += 1
        
        if same_place == CODE_SIZE:
            win = True
            print(f"You won! After {attempts} attempts.")
        else:
            print(f"Direct hits:     {same_place}")
            print(f"Not direct hits: {same_digits}")
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