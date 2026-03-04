year = int(input("Enter the year: "))

century = (year - 1) // 100 + 1

# Determine suffix
if 11 <= century % 100 <= 13:
    suffix = "th"
elif century % 10 == 1:
    suffix = "st"
elif century % 10 == 2:
    suffix = "nd"
elif century % 10 == 3:
    suffix = "rd"
else:
    suffix = "th"

print(f"{century}{suffix} century")