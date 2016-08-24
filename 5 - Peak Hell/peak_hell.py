import pickle
import requests

peaks_url = 'http://www.pythonchallenge.com/pc/def/banner.p'

peaks_hell = requests.get(peaks_url).text

# Unpickle response
data = pickle.loads(peaks_hell.encode())

for row in data:
    for char, times in row:
        print (char * times, end="")
    print ()
