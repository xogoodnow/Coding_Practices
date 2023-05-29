from itertools import product


def iterator():
    final = (list(product(F_list, S_list )))
    print (*final)


if __name__ == '__main__':

    a = input()
    b = input()

    F_list = [digit for digit in a.split()]
    S_list = [digit for digit in b.split()]


    iterator()

# from itertools import product
#
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
#
# print(*list(product(A, B)))