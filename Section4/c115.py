menu = [
    "egg bacon".split(),
    "egg sausage bacon".split(),
    "egg spam".split(),
    "egg bacon spam".split(),
    "egg bacon sausage spam".split(),
    "spam bacon sausage spam".split(),
    "spam sausage spam bacon spam tomato spam".split(),
    "spam egg spam spam bacon spam".split(),
]

# for meal in menu:
#     for index in range(len(meal) - 1, -1, -1):
#         if meal[index] == "spam":
#             del meal[index]
#     print(meal)
#

# generated code
for meal in menu:
    items = ", ".join((item for item in meal if item != "spam"))
    print(items)
