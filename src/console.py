import sys
from parse import *
from sequence import *
from desmos import *

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

        if cmd == "help":
            pass

        if cmd == "exit":
            sys.exit()

        # Multiple commands are comma separated
        cmds = cmd.split(', ')
        cmds[-1] = cmds[-1].replace(',', '')

        if not cmds[0].startswith("id"):
            print("First argument must be id.")
            continue

        sequence = Sequence()

        for i in cmds:
            i = i.split("=")

            cmd = i[0]
            arg = i[1]

            switch = {
                "id": parse_id,
                "name": parse_name,
            }
            func = switch.get(cmd, lambda x: None)
            func(arg, sequence)


if __name__ == '__main__':
    main()

