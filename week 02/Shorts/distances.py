distances = {
    "Voyager 1": 163,
    "Voyager 2": 136,
    "Pioneer 10": 80,
    "new Horizons": 58,
    "pioneer 11": 44
}

# use for loop to loop in sa dictionary keys
# def main():
#     for name in distances.keys():
#         print(f"{name} is {distances[name]} AU from Earth")

def main():
    for distance in distances.values():
        print(f"{distance} AU is  = {convert(distance)} m")

def convert(au):
    return au * 149597870700

main()