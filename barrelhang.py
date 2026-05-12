import random

# BarrelHang - 7 Stages (can scale back to 6 if needed)

stage_1 = r"""
  \\ | | //
    \| |/
     ___
    |   |
    |___|
"""

stage_2 = r"""
   \ | | /
     \|/
     ___
    |   |
    |___|
"""

stage_3 = r"""
    \| |
     \|
     ___
    |   |
    |___|
"""

stage_4 = r"""
     \|
      |
     ___
    |   |
    |___|
"""

stage_5 = r"""

    !!!!!
     ___
    |   |
    |___|
    (falling!)
"""

stage_6 = r"""

     ___
    |   |
    |___|
    ~~~~~~~
   (splash incoming!)
"""

stage_7 = r"""

  ~~ ___~~~
  ~~/ X |~~~
  ~~|_#_/~~~~
  ~~~~~~~~~~
  
  
    SPLASH!
"""

# Game setup

def guess_letter():
    letter_guessed = input("Guess a letter: ").lower()
    return letter_guessed


def check_valid_input(letter_guessed, old_letters_guessed): 
    if (len(letter_guessed) >= 2
         or not str.isalpha(letter_guessed)
         or not str.isascii(letter_guessed)
         or letter_guessed.lower() in old_letters_guessed):
        return False
    elif (str.isalpha(letter_guessed)
         and len(letter_guessed) == 1 
         and str.isascii(letter_guessed)
         and letter_guessed.lower() not in old_letters_guessed):
        return True
    
def try_update_letter_guessed(letter_guessed, old_letters_guessed): 
    checked_letter = check_valid_input(letter_guessed, old_letters_guessed)
    if checked_letter == False:
        separator = " -> "
        print("X")
        print(separator.join(old_letters_guessed))
        return False
    elif checked_letter == True:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    
def main():
    old_letters_guessed = []
    letter_guessed = guess_letter()
    post_check_letter = check_valid_input(letter_guessed, old_letters_guessed)
    print(post_check_letter)

print("Welcome to BarrelHang!")
print(f"You have 5 attempts to win.")
print(r"""
  ____                      _ _   _
 |  _ \                    | | | | |
 | |_) | __ _ _ __ _ __ ___| | |_| | __ _ _ __   __ _
 |  _ < / _` | '__| '__/ _ \ |  _  |/ _` | '_ \ / _` |
 | |_) | (_| | |  | | |  __/ | | | | (_| | | | | (_| |
 |____/ \__,_|_|  |_|  \___|_|_| |_|\__,_|_| |_|\__, |
                                                  _| |
                                                 |___|
""")
main()
