
import sys


def parseInt(s):
    try:
        return int(s)
    except:
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
        lStrNum = ''
        rNum = ''
        rStrNum = ''
        while l <= r:
            if len(lNum) > 0 and len(rNum) > 0:
                sum = sum + int(lNum+rNum)
                break
            if lNum == '':
                if parseInt(line[l]) != None:
                    lNum = line[l]
                else:
                    l += 1
            if rNum == '':
                if parseInt(line[r]) != None:
                    rNum = line[r]
                else:
                    r -= 1
    print(sum)


if __name__ == "__main__":
    main()
