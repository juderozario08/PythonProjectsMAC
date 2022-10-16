from random import randint

busTimes = []
time = 0

while time < 1440:
    time += randint(10, 20)
    if time < 1440:
        busTimes.append(time)

for i in busTimes:
    strTime = ""
    hour = i//60
    minutes = i % 60
    strTime += f"0{hour}" if hour <= 9 else f"{hour}"
    strTime += f":0{minutes}" if minutes <= 9 else f":{minutes}"
    print(strTime)
