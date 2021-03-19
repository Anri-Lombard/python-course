data = [3, 2, 342, 344, 543, 212, 345, 432, 234]

min_valid = 300
max_valid = 500

# # arrange from low to high
# data.sort()
#
# # process the lowest numbers
# stop = 0
# for index, value in enumerate(data):
#     if value >= min_valid:
#         stop = index
#         break
#
# print(stop)  # for debugging
# del data[:stop]
# print(data)
#
# # process the highest numbers
# start = 0
# # start at end, then finish at start (-1, otherwise index 0 is skipped)
# for index in range(len(data) - 1, -1, -1):
#     if data[index] <= max_valid:
#         # We have the index of the last item, now we set 'start' to
#         # position of the first. Item to delete is one after 'index'
#         start = index + 1
#         break

# much more effective code using less data
top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min_valid or max_valid < value:
        print(top_index - index, value)
        del data[top_index - index]

print(data)
