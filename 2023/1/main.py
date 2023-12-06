
import sys

DIGITS = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
]


def parseInt(s):
    try:
        return int(s)
    except:
        return None


def parseStringDigit(s, i, rtl=False):
    for digit in DIGITS:
        substr = s[::i] if rtl else s[i::]
        # make sure digit isn't too big
        if (len(digit) <= len(substr) and digit in substr):
            print(rtl, digit, substr)
            return i - len(digit) + 1 if rtl else i + len(digit) - 1
    return None


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        content = file.read()

    doc = content.split('\n')
    sum = 0
    for line in doc:
        l = 0
        r = len(line) - 1
        lNum = ''
        rNum = ''
        while l <= r:
            lStrDigit = parseStringDigit(line, l)
            rStrDigit = parseStringDigit(line, r, True)
            if len(lNum) > 0 and len(rNum) > 0:
                print(lNum, rNum)
                sum = sum + int(lNum+rNum)
                break
            if lNum == '':
                if parseInt(line[l]) != None:
                    lNum = line[l]
                elif lStrDigit != None:
                    lNum = line[l:lStrDigit]
                    l += lStrDigit
                else:
                    l += 1
            if rNum == '':
                if parseInt(line[r]) != None:
                    rNum = line[r]
                elif rStrDigit != None:
                    lNum = line[rStrDigit:r]
                    r -= rStrDigit
                else:
                    r -= 1
    print(sum)


if __name__ == "__main__":
    main()
