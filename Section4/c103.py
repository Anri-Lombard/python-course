data = [3, 2, 342, 344, 543, 212, 345, 432, 234]

min_valid = 300
max_valid = 500

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or max_valid < value:
        print(top_index - index, value)
        del data[top_index - index]

print(data)

# Deleting slices are more efficient than individual items.
