import os


def pangrams(s):
    abc = 'abcdefghijklmnopqrstuvwxyz'
    for i in abc:
        if i not in s.lower():
            return 'not pangram'
    return 'pangram'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()