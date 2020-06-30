import sys


def main():

    intro = \
      "DesmOEIS\n" \
      "A tool for converting OEIS sequences to Desmos lists.\n" \
      "\n" \
      "Type id=<OEIS id> (without the brackets) to convert a sequence. \n" \
      "Type help for a list of all valid commands. \n" \
      "Type exit to close the application. \n" \

    print(intro)

    while True:
        cmd = input()

        if cmd == "exit":
            sys.exit()


if __name__ == '__main__':
    main()

