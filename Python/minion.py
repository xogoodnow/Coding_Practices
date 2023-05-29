def minion_game(string):
    s = len(string)
    vowel = 0
    consonant = 0

    for i in range(s):
        if string[i] in 'AEIOU':
            vowel += (s - i)
        else:
            consonant += (s - i)

    if vowel < consonant:
        print('Stuart ' + str(consonant))
    elif vowel > consonant:
        print('Kevin ' + str(vowel))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(s)


    # def minion_game(string):
    # s = len(string)
    # vowels = 'AEIOU'
    # vowel_score = sum(s - i for i in range(s) if string[i] in vowels)
    # consonant_score = sum(s - i for i in range(s) if string[i] not in vowels)
    #
    # if vowel_score < consonant_score:
    # print(f"Stuart {consonant_score}")
    # elif vowel_score > consonant_score:
    # print(f"Kevin {vowel_score}")
    # else:
    # print("Draw")
    #
    # if __name__ == '__main__':
    # s = input()
    # minion_game(s)