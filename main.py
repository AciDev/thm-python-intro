from base64 import *


def main():
    file = open('./encodedflag.txt', 'r').read()

    for i in range(15):
        if i < 5:
            file = b16decode(file)
        elif i < 10:
            file = b32decode(file)
        else:
            file = b64decode(file)

    print(file.decode())


if __name__ == "__main__":
    main()
