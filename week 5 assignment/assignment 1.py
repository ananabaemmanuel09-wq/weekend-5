numbers = [1, 5, 7, 8, 10, 18, 50]
count = 0

for num in numbers:
    if num % 2 == 0:
        count += 1

print("The number of even is", count)