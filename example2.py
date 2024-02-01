# Sum all numbers 50 to 700
# Version 1

total = 0
n = 50

while n <= 700:
    total =  total + n
    n = n + 1
    if n < 60:
        print(n, total)

print(total)