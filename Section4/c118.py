numbers = '3,867,348,091,234,749,443'
print(numbers.split(","))

generated_list = [
    "9", " ", "2", "2", "3", " ", "3", "7", "2", " ", "0",
    "3", "6", " ", "8", "5", "6", " ", "8", "5", "4",
    " ", "7", "7", "5", " ", "8", "0", "7"
]

values = "".join(generated_list)
print(values)

values_list = values.split()
print(values_list)

for i in range(len(values_list)):
    values_list[i] = int(values_list[i])

print(values_list)
