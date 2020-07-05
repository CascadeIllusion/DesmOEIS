import requests


def parse_id(args):

    id = args.get("id")

    # Remove the preceding A if included
    id = id.replace('A', '')

    # Add trailing zeros if necessary
    length = len(id)
    if length < 6:
        for i in range(0, 6 - length):
            id = "0" + id

    # Add A at the beginning of the query
    id = 'A' + id

    return id


def find_id(id):

    url = f"https://oeis.org/search?q=id:{id}&fmt=text"
    r = requests.get(url)

    if "No results." in r.text:
        return None

    return r


def parse_integers(sequence):

    text = sequence.results.text

    text = str.splitlines(text)

    rows = []

    if sequence.args.get("ext") == "true":

        b_id = sequence.id.replace('A', 'b')
        url = f"https://oeis.org/{sequence.id}/{b_id}.txt"
        r = requests.get(url)
        sequence.results = r
        text = r.text
        text = str.splitlines(text)

        for line in text:
            space = line.find(" ")
            row = line[space + 1:]
            row = row.split(', ')
            rows.append(row)

    else:

        for line in text:
            if line.startswith('%S') or line.startswith('%T') or line.startswith('%U'):
                # integers start 11 characters into the line
                row = line[11:]
                row = row.split(',')
                rows.append(row)

    rows = [row for integer in rows for row in integer]

    # Remove empty elements resulting from commas at the end of the %S and %T rows
    rows = list(filter(None, rows))

    return rows
