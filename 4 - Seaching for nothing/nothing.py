"""Searching for nothing."""

import requests

# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}'

nothings_url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'
nothing = 12345

help_message = False
solution = ''

print ("Searching for nothing, wait a moment...")

while True:
    r = requests.get(nothings_url, {'nothing': nothing})
    nothing = r.text.split()[-1]
    try:
        nothing = int(nothing)
    except ValueError:
        if help_message:
            solution = nothing
            break
        help_message = True

next_url = base_url.format(solution=solution)
print (next_url)
