first_angle = int(input('Enter first angle of triangle: '))
second_angle = int(input('Enter second angle of triangle: '))

if (first_angle + second_angle) < 180:
    third_angle = 180 - (first_angle + second_angle)
    print(f"The third angle is: {third_angle} ")
else:
    print("Invalid angle.")