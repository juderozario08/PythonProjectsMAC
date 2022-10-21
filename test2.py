from subprocess import call


currentTime = input(
    "What time is it in 24 hour clock? \nExample: 00:00 \n").split(":")
arrivalTime = input(
    "What time do you need to be in school by? Same input format as last question: \n").split(":")
currentTime = int(currentTime[0]) + (int(currentTime[1])/60)
arrivalTime = int(arrivalTime[0]) + (int(arrivalTime[1])/60)


def getDifferenceInTime():
    return 24 + arrivalTime - currentTime if arrivalTime < currentTime else arrivalTime - currentTime


def callUber():
    return "Call an uber"


def uber__or_29():
    priority = input(
        "Is it absolutely necessary to reach school on time? yes or no: ").strip().upper()
    return callUber() if priority == 'yes' else "take 29 and bus 505"


def uber__or_63():
    priority = input(
        "Is it absolutely necessary to reach school on time? yes or no: ").strip().upper()
    return callUber() if priority == 'yes' else "take 63 and Line 1"


def eglinton():
    eglintonOpen = input(
        "Is Eglinton Station West open? Yes or No: ").strip().lower()
    return "Take bus 63 and Line 1" if eglintonOpen == 'yes' else "Take bus 90 and Line 1"


def rushHour():
    return 7 <= arrivalTime <= 9 or 17 <= arrivalTime <= 18


if 2 <= arrivalTime <= 7:
    if getDifferenceInTime() >= 2:
        print("Take bus 29 and bus 505")
    elif getDifferenceInTime() < 2:
        print(uber__or_29())

if 2 > arrivalTime > 7:
    if rushHour():
        print()
