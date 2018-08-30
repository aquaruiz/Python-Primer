fahrenheit = [e for e in range(0, 101, 10)]
celsius = [(e - 32) / 1.8 for e in fahrenheit]
approx_celsius = [(e - 30) / 2 for e in fahrenheit]

nested_list = [[f, c, a] for f, c, a in zip(fahrenheit, celsius, approx_celsius)]

for fahrenheit, celsius, approx_celsius in nested_list:
    print('%5.1fF = %5.1fC \u2248 %5.1fC' % (fahrenheit, celsius, approx_celsius))