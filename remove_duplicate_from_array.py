numbers = [4, 2, 6, 4, 8, 2, 9, 1, 6]

unique = []

for i in range(len(numbers)):
    found = False

    for j in range(len(unique)):
        if numbers[i] == unique[j]:
            found = True
            break

    if found == False:
        unique.append(numbers[i])

print("Original List:", numbers)
print("Unique List:", unique)
        