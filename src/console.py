import sys
from parsing import *
from desmos import *
from sequence import Sequence


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

        args = dict()

        for i in cmds:
            i = i.split("=")

            cmd = i[0]
            value = i[1]

            args[cmd] = value

        id = parse_id(args)

        results = find_id(id)

        if results:
            sequence = Sequence(id)
            sequence.args = args
            sequence.results = results
        else:
            print("Invalid id.")
            continue

        sequence.integers = parse_integers(sequence)

        create_expression(sequence.integers, sequence, create_desmos_list)


if __name__ == '__main__':
    main()

