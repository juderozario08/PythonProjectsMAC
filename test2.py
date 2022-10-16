# strings = ["apples", "banana", "clementine"]
# counter = 0
# vowels = 'aeiou'
# for string in strings:
#     for char in string:
#         if char in vowels:
#             counter += 1
# print(counter)

currentTime = input("What time is it in 24 hour clock? \nExample: 00:00 \n")
arrivalTime = input(
    "What time do you need to be in school by? Same input format as last question: \n")
currTimeArr = currentTime.split(":")
arrivalTimeArr = arrivalTime.split(":")
currTimeInMin = int(currTimeArr[0])*60 + int(currTimeArr[1])
arrivalTimeInMin = int(arrivalTimeArr[0])*60 + int(arrivalTimeArr[1])


def uber_or_not():
    priority = ''
    while True:
        priority = str(input(
            "Is it absolutely necessary for you to make it on time? Yes or No: \n")).replace(" ", "").lower()
        if priority == 'yes' or priority == 'no':
            break
    return "Call an uber" if priority == 'yes' else "Take bus 29 and bus 505"


if 120 <= arrivalTimeInMin <= 420:
    if arrivalTimeInMin - currTimeInMin >= 120:
        print("Take bus 29 and bus 505")
    elif arrivalTimeInMin - currTimeInMin < 120:
        print(uber_or_not())
