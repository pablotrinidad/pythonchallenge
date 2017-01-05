"""Warming up."""

# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

# Based on the problem image.
solution = 2 ** 38

next_url = base_url.format(solution=solution)
print (next_url)
