import requests


def parse_id(id=""):

    # Remove the preceding A if included
    id = id.replace('A', '')

    # Add trailing zeros if necessary
    length = len(id)
    if length < 6:
        for i in range(0, 6 - length):
            id = "0" + id

    # Add A at the beginning of the query
    id = 'A' + id

    url = f"https://oeis.org/search?q=id:{id}&fmt=text"
    r = requests.get(url)


def parse_name(cmd=""):
    print("PARSENAME")