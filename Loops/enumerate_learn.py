
menu = ["chai", "coffeee", "ginger tee", "burger tee"]

for m in menu:
    print(f"Menu item is {m}")

# But we can't print the number of these menu-items like "chai" is no.1 and "coffee" is no.2 and so on....


# So to overcome that we have enumerate

seasons = ["Spring", "Summer", "Fall", "Winter"]
list(enumerate(seasons))

# It becomes like this :
# [(0, "Spring"), (1, "Summer"), (2, "Fall"), (3, "Winter")]

# We can also do this:
list(enumerate(seasons, start=1))

# [(1, "Spring"), (2, "Summer"), (3, "Fall"), (4, "Winter")]


# For the above example we can do this :

for idx, item in enumerate(menu, start=1):
    print(f"Menu no: {idx}'s item is: {item}")