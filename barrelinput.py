response = input("Guess a letter: ")

if len(response) > 1 and (not response.isalpha() or not response.isascii()):
    print("E3")
elif not response.isalpha() or not response.isascii():
    print("E2")
elif len(response) > 1:
    print("E1")
elif response.isalpha() and response.isascii():
    print(f"{response.lower()}")