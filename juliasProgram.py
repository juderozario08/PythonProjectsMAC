currentTime = int(input("What time is it (in 24 hour clock)?: "))
arrivalTime = int(
    input("What time do you need to get to school by (in 24 hour clock)?: "))

# here are my functions yayyyy


def uber_or_29():
    priority = input(
        "Is it absolutely necessary for you to make it on time? Yes or No: ").lower()
    if priority == "yes":
        return "Call an Uber."
    elif priority == "no":
        return "Take bus 29 and bus 505."
    # else:
    # figure out how to create else condition that retakes input


def uber_or_63():
    priority = str(input(
        "Is it absolutely necessary for you to make it on time? Yes or No: ")).lower()
    if priority == "yes":
        return "Call an Uber."
    elif priority == "no":
        return "Take bus 63 and Line 1."
    # else:
    # figure out how to create else condition that retakes input


def eglinton():
    eglinton_open = input(
        "Is Eglinton Station West open? Yes or No?: ").lower()
    if eglinton_open == "yes":
        return "Take bus 63 and Line 1."
    elif eglinton_open == "no":
        return "Take bus 90 and Line 1."
    # else:
    # figure out how to create else condition that retakes input


# When arrival time is between 2 am and 7 am (subway not running)
if 2 < arrivalTime < 7:
    if arrivalTime - currentTime >= 1:
        print("Take bus 29 and bus 505.")
    elif (arrivalTime - currentTime) < 1:
        print(uber_or_29())


def getDifferenceInTime():
    if arrivalTime < currentTime:
        return 24 + arrivalTime - currentTime
    else:
        return arrivalTime - currentTime


# When arrival time is between 7 am and 2 am (subway is running)
if 7 <= arrivalTime or arrivalTime <= 2:
    if (7 <= arrivalTime <= 9) or (17 <= arrivalTime <= 18):
        if getDifferenceInTime() <= 2:
            print(uber_or_63())
        elif getDifferenceInTime() > 0.5:
            print(eglinton())
    else:
        rain = input("Is it raining? Yes or No: ").lower()
        if rain == "yes":
            if (arrivalTime - currentTime) >= 11/12:  # 55 mins
                print("Take bus 29 and Line 1")
            elif (arrivalTime - currentTime) < 11/12:
                print(eglinton())
        if rain == "no":
            print(eglinton())
