meters = int(input())
centimeters = meters * 100
inches = centimeters / 2.54
feet = inches / 12
yards = feet / 3
british_miles = yards / 1760
print("A length of %d meters corresponds to %.2f inches, %.2f feet, %.2f yards, or %.4f miles."
      % (meters, inches, feet, yards, british_miles))
