"""Zip files."""

import zipfile

# Base URL.
nothing = '90052' # Initial value as suggested on the README.txt file

folder = zipfile.ZipFile('channel.zip')

solution = ''

while True:
    nothing_file = folder.open(nothing + '.txt')
    info = folder.getinfo(nothing + '.txt')
    nothing = nothing_file.read().split()[-1].decode()

    solution += info.comment.decode()

    if not nothing.isdigit():
        break

print (solution)
