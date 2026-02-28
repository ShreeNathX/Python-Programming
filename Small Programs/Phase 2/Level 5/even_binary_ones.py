n = int(input("Enter n: "))

for num in range(1, n + 1):
    binary = bin(num)[2:]        # convert to binary (remove '0b')
    ones_count = binary.count('1')

    if ones_count % 2 == 0:
        print(num, "->", binary)