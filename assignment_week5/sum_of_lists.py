def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = sum_list(my_list)

print("Sum =", result)