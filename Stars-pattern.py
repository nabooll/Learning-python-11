# We just gonna use for and while here!
def stars_patterns():
    stars = int(input("How many stars do you want to make: "))
    for i in range(stars):
        for j in range(i+1):
            print("*", end="")
        print("")
    return
stars_patterns()