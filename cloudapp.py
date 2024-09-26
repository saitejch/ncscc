def guess_game():
    number_to_guess = 7
    guess = int(input("Guess the number (1-10): "))
    if guess < 1 or guess > 10:
        print("Out of range! Please guess between 1 and 10.")
    elif guess < number_to_guess:
        print("Too low!")
    elif guess > number_to_guess:
        print("Too high!")
    else:
        print("Congratulations! You guessed it!")

if __name__ == "__main__":
    guess_game()
