import math
number = int(input("Please enter the number: "))

def evenorodd():
    rmd = math.remainder(number, 2)
    print(f"{rmd}")
    if rmd != 0:
        print ("Weird")
    elif rmd == 0 and number in range(2, 6):
        print("Not Weird")
    elif rmd == 0 and number in range(6, 21):
        print("Weird")
    elif rmd == 0 and number > 20:
        print ("Not Weird")
    else:
        print ("who can say where the road goes? ")

evenorodd()