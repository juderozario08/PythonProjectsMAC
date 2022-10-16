from sys import exit

# Using a dictionary to print the values with the number of coins used

def main():
    amount = int(100 * getpositivefloat())
    coins = [25, 10, 5, 1]
    dictchanges = {}
    counter = 0
    for coin in coins:
        dictchanges[coin] = check_value(coin, amount)
        while (amount >= coin):
            amount -= coin
            counter += 1

    print(dictchanges)
    
def check_value(coin, amount):
    counter = 0
    while amount >= coin:
        amount -= coin
        counter += 1
    return counter
    
def getpositivefloat():
    number = -1
    while number < 0:
        number = float(input("Input Change: "))
    return number

main()