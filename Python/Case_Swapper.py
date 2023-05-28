
def swap_case(s):

    letters=[ i for i in s]
    changed=[]
    for i in letters:
        u=i.upper()
        l=i.lower()
        if i==l:
            changed.append(i.upper())
        else:
            changed.append(i.lower())
    final=''.join(changed)
    return final

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)