# DesmOEIS
A command-line utility for converting OEIS (On-Line Encyclopedia of Integer Sequences) sequences into Desmos lists.

## Installation
`pip install desmoeis`

## Running
`cd` to `<path>/DesmOEIS/src`, where `<path>` is the path to your DesmOEIS folder. Then execute `python console.py`.

## Commands

**Syntax: (Command Name)=(Argument)**

**id:** Attempts to convert an OEIS id argument into a Desmos list. 
The "A" is optional, and trailing zeros may be excluded.

**name:** Assigns the resulting Desmos list to a variable with the given name. 
Names must be exactly one letter character (except "e"), no numbers or special characters.

**trim:** Filters a list using Python-style slicing syntax. For A:B:C:
A is the starting index (inclusive), default 0.
B is the ending index (exclusive), default is the list length.
C is a step value that is used to skip every C elements, default is 1 (don't skip anything).

**ext:** Pass Y to this to output the extended version of the OEIS sequence.
WARNING: Passing an entire extended sequence this way is usually not a good idea, as such
sequences can be hundreds of elements long, and can cause your browser to hang. You may want
to combine this with trimming syntax to reduce the number of elements.

**view:** Opens the .html file containing the last converted sequence since starting the program. 
Does not work if used before converting a sequence.

**help:** View a list of all valid commands.

**exit:** Closes the application.

## Links
[On-Line Encyclopedia of Integer Sequences](https://oeis.org/)

[Desmos](https://www.desmos.com/)
