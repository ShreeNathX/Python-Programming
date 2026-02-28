num = input("Enter any number: ")

for i in range(len(num)):
    if num[i] == '0':
        continue
    else:
        print(num[i])