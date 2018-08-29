fahrenheit = range(0, 101, 10)
celsius = [(e - 32) / 1.8 for e in fahrenheit]
approx_celsius = [(e - 30) / 2 for e in fahrenheit]


for fahrenheit, celsius, approx_celsius in zip(fahrenheit, celsius,approx_celsius):
    print('%5.1fF = %5.1fC \u2248 %5.1fC' % (fahrenheit, celsius, approx_celsius))