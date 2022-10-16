def boilingWater():
    b = int(input())
    pressure = (5*b) - 400
    print(pressure)
    if pressure > 100:
        print("-1")
    elif pressure < 100:
        print("1")
    else:
        print("0")

boilingWater()