from random import randint
from sys import exit

def get_guess():
    try:
        return int(input("Input Guess: "))
    except ValueError as error:
        print(error)

def close_call(number, guess):
    for i in [1, 2, 3, 4, 5]:
        if (number - i) == guess or (number + i) == guess:
            return "Close Call!!"
    return "Not Close Enough!!"

def hints(number, guess, counter):
    if counter == 2:
        randomness = randint(10, 90)
        print(check_odd_or_even_and_value(number, randomness, guess))
    elif counter == 3:
        print(f"The number is between {number - randint(5, 10)} and {number + randint(5, 10)}.")
    elif counter == 4:
        print(f"The number is between {number - randint(1, 4)} and {number + randint(1, 4)}.")
    elif counter == 5:
        factors(number)
        print()

def check_odd_or_even_and_value(number, randomness, guess):
    if (number<randomness and number%2 == 0) and number != guess:
        return "The number is less than {} and even.".format(randomness)
    elif (number>randomness and number%2 == 0) and number != guess:
        return "The number is greater than {} and even.".format(randomness)
    elif (number<randomness and number%2 != 0) and number != guess:
        return "The number is less than {} and odd.".format(randomness)
    elif (number>randomness and number%2 != 0) and number != guess:
        return "The number is greater than {} and odd.".format(randomness)

def factors(number):
    print("Factors are: ", end = "")
    for i in range(1, number):
        if number % i == 0:
            print(f"|{i}| ", end = "")

if __name__ == "__main__":
    stop = False
    while stop == False:
        number = randint(1, 100)
        counter = 1
        guess = -1
        while guess != number and counter <= 6:
            guess = get_guess()
            if number != guess:
                print(close_call(number, guess))
                hints(number, guess, counter)
            counter += 1
        if guess == number:
                print(f"You got it correct!! The number is {number}")
        elif counter > 6 and number != guess:
            print(f"You ran out of guesses!! The word was {number}")
        choice = str(input("Do you want to continue y/n: "))
        if choice == 'n':
            print("Ok Cool! Have a nice day...")
            exit()
        else:
            stop = False