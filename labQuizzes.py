def snacktorial(number):
    if number <= 0:
        return 0
    if 0 < number <= 1:
        return number
    return float(number*snacktorial(number-1))


# print(snacktorial(2.5))
# print(snacktorial(3.14159))
# print(snacktorial(4))
# print(snacktorial(-3.3))

def RecursiveAndOrFlip(ls):
    if len(ls) == 0:
        return 0
    if len(ls) == 1:
        return not ls[0]
    if len(ls) % 2 == 1:
        return RecursiveAndOrFlip(ls[0:len(ls)//2 + 1]) and RecursiveAndOrFlip(ls[len(ls)//2 + 1:len(ls)])
    return RecursiveAndOrFlip(ls[0:len(ls)//2]) or RecursiveAndOrFlip(ls[len(ls)//2: len(ls)])


# print(RecursiveAndOrFlip([True, False]))
# print(RecursiveAndOrFlip([True, False, False]))
# print(RecursiveAndOrFlip(
#     [False, False, True, False, True, True, False, True, True]))

teletubbies = ["Tinky Winky", "Dipsy", "Laa-Laa", "Po"]


def teletubby(string):
    if string in teletubbies:
        return [string]
    teletub = ""
    for i in teletubbies:
        if i in string:
            teletub = i
            return [teletub]+(teletubby(string[len(teletub): len(string)]))


# print(teletubby("PoPo"))
# print(teletubby("Tinky Winky"))
# print(teletubby("Laa-LaaLaa-LaaLaa-Laa"))
# print(teletubby("DipsyDipsyDipsyDipsy"))
