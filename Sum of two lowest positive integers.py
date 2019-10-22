def sum_two_smallest_numbers(numbers):
    numbers.sort()
    if type(numbers[0]) and type(numbers[1]) is int:
        sum = numbers[0]+numbers[1]
    return sum