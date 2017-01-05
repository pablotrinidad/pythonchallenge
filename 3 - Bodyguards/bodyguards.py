"""Bodyguards."""

# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

# Read file as content
f = open('characters.txt', 'r')
text = f.read().replace('\n', '')

solution = ''

for i in range(len(text)):
    if (
        # Check for the 4th letter to the left to be lower case.
        text[i-4: i-3].islower() and

        # Check for the 3 letters on it's left side to be upper case.
        text[i-3: i].isupper() and

        # Check the current letter is lower case.
        text[i].islower() and

        # Check for the 3 letters on it's right side to be upper case.
        text[i+1: i+4].isupper() and

        # Check for the 4th letter to the right to be lower case.
        text[i+4: i+5].islower()):

        solution += text[i]

next_url = base_url.format(solution=solution)
print (next_url)
