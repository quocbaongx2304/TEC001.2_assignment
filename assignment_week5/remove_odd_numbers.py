def remove_odd(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list
    
original_list = [1, 2, 3, 4, 5, 6, 7, 8]
new_list = remove_odd(original_list)

print("Original list:", original_list)
print("Even numbers only:", new_list)