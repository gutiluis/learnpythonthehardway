four_things = "Gun Bazooka Bombs Missiles"

print("Wait there are not 4 things in that list. Fix that.")

stuff = four_things.split(" ")
more_stuff = ["Death", "Kill", "Murder", "Happiness",
            "Genocide", "Banana", "Country", "Tank"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(" ".join(stuff))
print("#".join(stuff[3:5]))
