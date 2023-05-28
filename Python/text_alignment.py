hugeness = int(input()) #This must be an odd number
char = 'H'
for i in range(hugeness):
    print((char*i).rjust(hugeness-1)+char+(char*i).ljust(hugeness-1))

for i in range(hugeness+1):
    print((char*hugeness).center(hugeness*2)+(char*hugeness).center(hugeness*6))

for i in range((hugeness+1)//2):
    print((char*hugeness*5).center(hugeness*6))

for i in range(hugeness+1): print((char*hugeness).center(hugeness*2)+(char*hugeness).center(hugeness*6))

for i in range(hugeness):  print(((char*(hugeness-i-1)).rjust(hugeness)+char+(char*(hugeness-i-1)).ljust(hugeness)).rjust(hugeness*6))