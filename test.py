# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# col_index = 1

# # Transpose the list using zip
# transposed = list(zip(*my_list))

# # Reverse the desired column
# transposed[col_index] = reversed(transposed[col_index])

# # Transpose back to original form
# my_list = list(zip(*transposed))

# print(my_list)

# print((1, 2, 3))
names = [["Alice", "Bob", "Charlie"], [1, 2, 3]]
ages = [25, 30, 35]

zipped = zip(*names)

print(list(zipped))
