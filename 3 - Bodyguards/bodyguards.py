# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

# Read file as content
f = open('characters.txt', 'r')
text = f.read().replace('\n', '')

solution = ''

for i in range(len(text)):
    if (
        # Check the 4th man ah the left is lower.
        text[i-4: i-3].islower() and

        # Check the 3 left side bodyguards are upper.
        text[i-3: i].isupper() and

        # Check the VIP's lower.
        text[i].islower() and

        # Check the 3 right side bodyguards are upper.
        text[i+1: i+4].isupper() and

        # Check the 4th man at the right is lower.
        text[i+4: i+5].islower()):

        solution += text[i]

next_url = base_url.format(solution=solution)
print (next_url)
