# I'm just gonna do just like before
stars = int(input("How many stars do you want to make: "))

def stars_patterns():
    for i in range(1, stars + 1): # Loop through rows
        print(" " * (stars - i), end="") # Print spaces for alignment (optional)
        print("* " * i) # Print stars for the current row
    return

stars_patterns()
