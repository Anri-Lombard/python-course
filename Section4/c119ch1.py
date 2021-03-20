user_input = input("Please enter your three numbers in the form of"
                   " a,b,c where a, b, and c are numbers: ")
number_list = user_input.split(",")

for index in range(len(number_list)):
    number_list[index] = int(number_list[index])

calculated_value = number_list[0] + number_list[1] - number_list[2]

print(calculated_value)
