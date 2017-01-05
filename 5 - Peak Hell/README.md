# 5 - Peak Hell

**Hint**:

Ok, this is a tricky one...

The web page's hint is telling us to *PRONOUNCE IT*, and while the whole
key remains in this simple instruction, we still need to write down some code.

By looking at the source code, we will see the following comment:

```<!-- peak hell sounds familiar ? -->```

As well as an invalid HTML tag (`<peakhell />`) referencing a source 
named [`banner.p`](http://www.pythonchallenge.com/pc/def/banner.p).

**Solution**:

If we keep pronouncing _"Peak hell"_ we'll notice that it sound like _"Pickle"_ 
(Yes, that thing swimming on vinegar)

![Fucking pickles!](https://img.buzzfeed.com/buzzfeed-static/static/2015-03/31/1/enhanced/webdr02/enhanced-7879-1427781273-1.jpg)

When we search for _"pickle python"_ in Google's search engine we'll find out that it's actually [a method
for serializing](https://docs.python.org/3/library/pickle.html) python objects to byte
 streams called "_pickle_".

"_Pickled_" objects can be also _"unpickled"_ so we are able to obtain the original object.
In order to _"unpickle"_ something we can use the pre-loaded library `pickle` and do something like this:

```
import pickle

message = b"SOME WEIRD RANDOM CHARACTERS (BYTES STREAM)"
data = pickle.loads(message)
```

After _"unpiclking"_ our [`banner.p`](http://www.pythonchallenge.com/pc/def/banner.p) 
we are going to obtain a list o lists which will contain tuples with two values: 
A character (either '#' or ' ') and a integer. This is art! (Literally art).

We're also going to notice that the length of the parent lists are not always the same, 
but the first and the last one have only one tuple which looks like this `(' ', 95)`.

Furthermore, if we decide to add all the integers inside tuples for each parent list 
we're always going to have **95** as the final result.

So yeah we have a matrix, and the way to fill it up is multiplying the first element of each 
tuple (which is a character) by the second one (which is a number). And guess what, it says **channel**.

![Channel!](https://github.com/pablotrinidad/pythonchallenge/blob/master/5%20-%20Peak%20Hell/solution.png?raw=true)

We can go:

**From**: [http://www.pythonchallenge.com/pc/def/**peak**.html](http://www.pythonchallenge.com/pc/def/peak.html)

**To**: [http://www.pythonchallenge.com/pc/def/**channel**.html](http://www.pythonchallenge.com/pc/def/channel.html)

