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
            # So, for each module mass, calculate its fuel and add it to the total.
            # Then, treat the fuel amount you just calculated as the input mass and
            # repeat the process, continuing until a fuel requirement is zero or negative
            fuel = recursive_total_fuel_calculation(fuel, int(mass))
        print("Total fuel {}" .format(fuel))

            

def recursive_total_fuel_calculation(fuel, mass):
    input_mass = math.floor(int(mass)/3) - 2
    if input_mass < 0:
        return fuel
    else:
        fuel += input_mass
        return recursive_total_fuel_calculation(fuel, input_mass)


if __name__ == '__main__':
    main()
