import sys

CUBE_LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main():
    idSum = 0
    powerSum = 0
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        content = file.read()

    for game in content.split('\n'):
        gameSet = parseGame(game)
        if isPossibleGame(gameSet):
            idSum += getGameId(game)
        fewest = findMaximums(gameSet)
        powerSum += calcPower(fewest)
    return idSum, powerSum


def isPossibleGame(gameSet):
    # For each set in game, count the number of cubes and return count > limit foreach color
    # How game works: for each set, grab handful of cubes, show them, then put back in bag
    for gs in gameSet:
        for handful in gs:
            count, color = getCountAndColor(handful)
            if color not in CUBE_LIMITS.keys():
                return False
            if count > CUBE_LIMITS[color]:
                return False
    return True


def getCountAndColor(handful):
    countAndColor = handful.split(' ')
    return int(countAndColor[0]), countAndColor[1]


def parseGame(s):
    subStr = s.split(': ')[1]
    subStr = subStr.split(';')
    x = []
    for subSubStr in subStr:
        x.append(subSubStr.strip().split(', '))
    return x


def getGameId(s):
    subStr = s.lstrip('Game ')
    i = 0
    gId = ''
    while (subStr[i].isdigit()):
        gId = gId + subStr[i]
        i += 1
    return int(gId)


def findMaximums(gameSet):
    maximums = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for gs in gameSet:
        for handful in gs:
            count, color = getCountAndColor(handful)
            if color in maximums.keys():
                maximums[color] = max(maximums[color], count)
    return maximums


def calcPower(maximums):
    return maximums['red'] * maximums['blue'] * maximums['green']


if __name__ == "__main__":
    print(main())
