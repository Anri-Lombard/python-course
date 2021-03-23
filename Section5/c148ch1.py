def sum_eo(n, t):
    sum_of_even_numbers = 0
    sum_of_odd_numbers = 0
    for i in range(n):
        if i % 2 == 0:
            sum_of_even_numbers += i
        elif i % 2 != 0:
            sum_of_odd_numbers += i

    if t == "e":
        return sum_of_even_numbers
    elif t == "o":
        return sum_of_odd_numbers
    else:
        return -1


print(sum_eo(10, "e"))
print(sum_eo(7, "o"))
print(sum_eo(11, "spam"))
