# TUPLES

# for tplIndex, tplCharacter in enumerate("abcdefg"):
#     print(tplIndex, tplCharacter)
#
# table = ("Coffee table", 200, 100, 75, 43.50)
#
# # Tuples make it useful to read code easily by unpacking it.
# name, length, width, height, price = table
# print(length * width)

albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975),
    ("Bad Company", "Bad Company", 1974),
    ("Nightflight", "Budgie", 1981),
    ("More Mayhem", "Emilda May", 2011),
    ("Ride the Lightning", "Metallica", 1884)
]

for name, artist, year in albums:
    print(f"Albums: {name}, Artist: {artist}, Year: {year}")

# If user input is used to add songs to add songs, then a list should
# be used since tuples are immutable.
