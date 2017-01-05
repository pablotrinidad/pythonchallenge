"""Making translations."""

# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

# Shift cipher applied with 2 as key
hint = 'map'
solution = ''.join(chr(ord(x) + 2) for x in list(hint))

next_url = base_url.format(solution=solution)
print (next_url)
