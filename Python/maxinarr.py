n = int(input())
arr = list(map(int, input().split()))

max_val=max(arr)

newarr = [x for x in arr if x != max_val]

print (max(newarr))