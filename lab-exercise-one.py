# Distance Conversion Lab

def main():
    m = float(input('Enter the number of miles: '))

    print(f'\nNumber of Kilometers: {convertKm(m)} kilometers')
    print(f'Number of Yards: {convertYd(m)} yards')
    convertFt(m)

def convertKm(m):
    return (m * 1.61)

def convertYd(m):
    return (m * 1760)

def convertFt(m):
    print(f'Number of Feet: {m * 5280} feet')

main()