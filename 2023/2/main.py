import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]

    with open(filename, 'r') as file:
        content = file.read()

    games = content.split('\n')
    return


if __name__ == "__main__":
    main()
