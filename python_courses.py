fruits = ["cherry", "melone", "pineapple","banana", "peach","apple",]


# print(fruits.sort());
# print(fruits)

even_numbers = [2,4,6,12,64,8,10,5,54,16]
# print(even_numbers.sort())
# print(even_numbers)

# def greater_than_five (n):
#   return n > 5

# print(even_numbers.sort(key = greater_than_five))
# print(even_numbers)

# copy_even_numbers = even_numbers.copy()
# print(even_numbers);
# print(copy_even_numbers);
# print(list(fruits))

copy_fruits = fruits[:]
# joined_lists = copy_fruits + even_numbers
copy_fruits.extend(even_numbers)
print(copy_fruits)