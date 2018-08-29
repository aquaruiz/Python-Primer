fahrenheit = range(0, 101, 10)
celsius = [(e - 32) / 1.8 for e in fahrenheit]

for fahrenheit, celsius in zip(fahrenheit, celsius):
    print('%5.1fF = %5.1fC' % (fahrenheit, celsius))