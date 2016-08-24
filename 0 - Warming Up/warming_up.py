# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

# Based on the problem image.
e = 2 ** 38

solution = base_url.format(solution=e)
print (solution)
