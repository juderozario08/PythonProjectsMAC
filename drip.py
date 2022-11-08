def outfit():
    colors = ["yellow", "orange", "red", "purple", "blue", "green"]
    apparel = ["shirt", "pants", "dress", "sweater"]
    userColors = []
    userApparels = []
    fits = []
    stop = False
    while not stop:
        color = ''
        clothing = ''
        while not stop:
            color = input("Enter a valid color: ").strip()
            if color in colors:
                break
            if color == 'stop':
                stop = True
        while not stop:
            clothing = input("Enter a valid apparel: ").strip()
            if clothing in apparel:
                break
            if clothing == 'stop':
                stop = True
        if not stop:
            userColors.append(color)
            userApparels.append(clothing)
            fits.append(f"{color} {clothing}")
    print(f"Input:\n{fits}\nOutput:")
    return [userColors, userApparels]


def drip():
    outputs = outfit()
    colors = outputs[0]
    apparels = outputs[1]
    fits = {}
    for i in range(len(colors)):
        fits[colors[i]] = apparels[i]
    if 'yellow' in colors and 'purple' in colors:
        if fits['yellow'] != fits['purple']:
            return "Nice Fit"
    elif 'blue' in colors and 'orange' in colors:
        if fits['blue'] != fits['orange']:
            return "Nice Fit"
    elif 'green' in colors and 'red' in colors:
        if fits['green'] != fits['red']:
            return "Nice Fit"
    return "Zero Drip"


if __name__ == '__main__':
    print(drip())
