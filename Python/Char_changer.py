word = input()
letters = list(word)
desired = input()
des = list(desired)
print(des)

def changer():
    a = int(des[0])
    print(a)
    letters[a] = des[2]
    final = ''.join(letters)
    return final

result = changer()
print(result)
