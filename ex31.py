print("""You enter a dark room with three doors for now.
Do you go through door #1, door #2, or door #3""")

door = input(">  ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input(">  ")
    # if inside if
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is probably better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input(">  ")
    # if inside if
    if insanity == "1" or instanity == "2":
        print("Your body survive powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")
elif door == "3":
    print("Kill everybody.")
    print("Choose a weapon:")
    print("1. Bazooka")
    print("2. Granade")

    weapon = input("> ")
    if weapon == "1":
        print("Kill all the monkeys with the bazooka.")
    elif weapon == "2":
        print("Kill all the monkeys with the granade.")
    else:
        print("The monkeys will kill you.")
else:
    print("You stumble around and fall on a knife and die. Good job!")
