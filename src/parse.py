import requests
from sequence import *
from desmos import *


def parse_id(id, sequence):

    # Remove the preceding A if included
    id = id.replace('A', '')

    # Add trailing zeros if necessary
    length = len(id)
    if length < 6:
        for i in range(0, 6 - length):
            id = "0" + id

    # Add A at the beginning of the query
    id = 'A' + id

    sequence.id = id

    url = f"https://oeis.org/search?q=id:{id}&fmt=text"
    r = requests.get(url)

    if "No results." in r.text:
        print("Invalid id.")
        return

    text = str.splitlines(r.text)

    parse_integers(text, sequence)


def parse_integers(text, sequence):

    rows = []

    for line in text:
        if line.startswith('%S') or line.startswith('%T') or line.startswith('%U'):
            # integers start 11 characters into the line
            row = line[11:]
            row = row.split(',')
            rows.append(row)

    # Flatten all three rows into one list
    rows = [row for integer in rows for row in integer]

    # Remove empty elements resulting from commas at the end of the %S and %T rows
    rows = list(filter(None, rows))

    sequence.integers = rows

    create_expression(rows, sequence, create_desmos_list)


def parse_name(name, sequence):

    if len(name) > 1:
        print("Variable names must be one character only.")
        return

    if str.isdecimal(name) or name == 'e':
        print("Numeric names and the constant e (2.71828...) are not allowed.")
        return

    name = f"{name}="

    sequence.name = name

    attach_name(name, sequence)
