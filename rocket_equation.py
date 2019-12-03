import sys
import os
import math


def main():
    filepath = sys.argv[1]

    if not os.path.isfile(filepath):
        print("File path {} does not exist. Exiting...".format(filepath))
        sys.exit()

    with open(filepath) as fp:
        fuel = 0
        for mass in fp:
            # To find the fuel required for a module, take its mass, divide by three, round down, and subtract 2
            fuel += math.floor(int(mass)/3) - 2
    print(fuel)


if __name__ == '__main__':
    main()
