# Immutable objects in python: int, float, decimal, bool, string, tuple,
# and range.

result = "Correct"
another_result = result
print(id(result))
print(id(another_result))

result += "ish"
print(id(result))
# id is different.
