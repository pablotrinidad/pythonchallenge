# 1 - What about making trans?

**Hint**:

![map](http://www.pythonchallenge.com/pc/def/map.jpg)

**Solution**:

The key for obtaining the solution is to focus on the _distance_ between letters on the image (which is 2), so we can assume
that the hint below can be _"encrypted"_ using a [substitution cipher](https://en.wikipedia.org/wiki/Substitution_cipher).

_"Decrypting"_ the message below will result on:

> I hope you didn't translate it by hand. That's what computers are for. Doing it in by hand is inefficient and that's why this text is so long. using string.maketrans() is recommended. now apply on the url.

We do so and the URL will change:
    
**From**: [http://www.pythonchallenge.com/pc/def/**map**.html](http://www.pythonchallenge.com/pc/def/map.html)

**To**: [http://www.pythonchallenge.com/pc/def/**ocr**.html](http://www.pythonchallenge.com/pc/def/ocr.html)

> M -> O

> A -> C

> P -> R
