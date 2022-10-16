import sys
# Main function executes all the functions
def main():
    ccn = int(input("Credit Card Number: "))
    length = len(str(ccn))
    if length < 13:
        print("INVALID")
    validity = check_validity(ccn)
    if validity is False:
        print("INVALID")
        sys.exit()
    else:
        print_card(length, ccn)

# Checking the validity of the Card Number
def check_validity(card):
    total_sum = 0
    position = 0
    while card != 0:
        if position % 2 == 0:
            total_sum += card % 10
        else:
            temp = 2 * (card % 10)
            if temp > 9:
                total_sum += (int(temp / 10)) + (temp % 10)
            else:
                total_sum += temp
        card = int(card / 10)
        position += 1
    if total_sum % 10 != 0:
         return False
    else:
        return True

# Print the card according to the number and the length
def print_card(length, card):
    while card >= 100:
        card = int(card / 10)
    if (card == 34 or 37) and length == 15:
        print("AMEX", end= "")
    elif card in [51, 52, 53, 54, 55] and length == 16:
        print("MASTERCARD", end= "")
    elif (length == 13 or 16) and int(card/10) == 4:
        print("VISA", end= "")
    else:
        print("INVALID", end= "")
    return

# Execute main
main()
