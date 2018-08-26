volume = 1  # 1 liter
volume = volume * 1000  # in cubic cm cm3


def read_densities(filename):
    infile = open(filename, 'r')
    densityes = {}
    for line in infile:
        words = line.split()
        dens = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densityes[substance] = dens
    infile.close()
    return densityes


densities = read_densities('densities.dat')

for name, density in densities.items():
    mass = density * volume / 1000
    print("%s density %g g/cm3 mass per liter %g kg" % (name, density, mass))
