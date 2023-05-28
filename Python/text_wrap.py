import textwrap


def wrap(string, max_width):
    sentences = textwrap.wrap(string, max_width)
    for line in sentences:
        print(line)



if __name__ == '__main__':
    string = str(input())
    max_width = int(input())
    wrap(string, max_width)