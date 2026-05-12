
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

def guess_letter():
    """Prompt the user to guess a letter, return it lowercase."""
    letter_guessed = input("Guess a letter: ").lower()
    return letter_guessed


def check_valid_input(letter_guessed, old_letters_guessed):
    """Check if guessed letter is a single English and not guessed before."""
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
    """Uses check_valid_input to check if guessed letter is valid,
    if yes, add to old_letters_guessed and return True,
    else print 'X' and sorted list of guessed letters and return False."""
    checked_letter = check_valid_input(letter_guessed, old_letters_guessed)
    if checked_letter == False:
        separator = " -> "
        print("X")
        print(separator.join(sorted(old_letters_guessed)))
        return False
    elif checked_letter == True:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    
def main():
    old_letters_guessed = []
    letter_guessed = guess_letter()
    post_check_letter = try_update_letter_guessed(letter_guessed, old_letters_guessed)
    print(post_check_letter)
# -- Test calls --
# old_letters = ['a', 'p', 'c', 'f']
# try_update_letter_guessed('A', old_letters)   # X, sorted list, False
# try_update_letter_guessed('s', old_letters)   # True
# try_update_letter_guessed('$', old_letters)   # X, sorted list, False
# try_update_letter_guessed('d', old_letters)   # True


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
