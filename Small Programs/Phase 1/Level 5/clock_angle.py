h = int(input("Enter hours: "))
m = int(input("Enter minutes: "))

# Convert 12 to 0
if h == 12:
    h = 0

minute_angle = 6 * m
hour_angle = (30 * h) + (0.5 * m)

angle = abs(hour_angle - minute_angle)

smaller_angle = min(angle, 360 - angle)

print("Smaller angle between hour and minute hands:", smaller_angle, "degrees")