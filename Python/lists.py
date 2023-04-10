N = int(input())

arra=[]


for _ in range(N):
    command=input().strip().split()
    cmd=command[0]
    if cmd == "append":
        valuee = int(command[1])
        arra.append(valuee)
    elif cmd == "print":
        print(arra)

    elif cmd == "remove":
        valuee = int(command[1])
        arra.remove(valuee)
    elif cmd == "pop":
        
        arra.pop()
    elif cmd == "sort":
        arra.sort()
    elif cmd == "reverse":
        arra.reverse()
    elif cmd == "insert":
        valuee = int(command[2])
        position = int(command[1])
        arra.insert(position, valuee)
    else:
        print("whaatt??")




    

    


