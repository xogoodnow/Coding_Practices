def analyzer(s):
    alphanumeric = any(c.isalnum() for c in s)
    alphabetical = any(c.isalpha() for c in s)
    digits = any(c.isdigit() for c in s)
    lowercase = any(c.islower() for c in s)
    uppercase = any(c.isupper() for c in s)

    print(alphanumeric)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

if __name__ == '__main__':
    s = input()
    analyzer(s)
