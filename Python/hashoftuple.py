n = int(input())
int_list = map(int, input().split())
t = tuple(int_list)
print(hash(t))
    

