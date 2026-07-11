def second_largest(numbers):

    if numbers[0] > numbers[1]:
        largest = numbers[0]
        second_largest = numbers[1]
    else:
        largest = numbers[1]
        second_largest = numbers[0]

    for i in range(2, len(numbers)):

        if numbers[i] > largest:
            second_largest = largest
            largest = numbers[i]

        elif numbers[i] > second_largest:
            second_largest = numbers[i]

    print("Largest Number:", largest)
    print("Second Largest Number:", second_largest)


numbers = [7, 4, 9, 12, 5, 15, 11]

second_largest(numbers)