# Base URL.
base_url = 'http://www.pythonchallenge.com/pc/def/{solution}.html'

# Read file as content
f = open('characters.txt', 'r')
text = f.read()

# Extract alphabet characters from file content
solution = ''.join([x for x in text if x.isalpha()])

next_url = base_url.format(solution=solution)
print (next_url)
