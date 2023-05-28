def sub_finder(word, sec_word):
    count = 0
    for i in range(len(word)):
        if word[i:].startswith(sec_word):
            count += 1
    print(count)

if __name__ == '__main__':
    word = input()
    sec_word = input()
    sub_finder(word, sec_word)