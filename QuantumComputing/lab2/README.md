

## Lab 2

###  Grover’s algorithm

This time, we're gonna try to implement simple algorithm using quantum gates learned in the lab 1.  
If you get stuck at some point or you're just lazy, there is [Jupiters Notebook](quantum3.ipynb) prepared for you.

> **_NOTE:_**  This lab is based on [this medium article by Jonathan Hui](https://medium.com/@jonathan_hui/qc-grovers-algorithm-cd81e61cf248), I highly recommend to read that before jumping into implementation

-----

At first we should get some intuition about Grover’s algorithm, it is a algorith that finds with *high probability* (not for sure!) the unique input to a black box function that produces a particular output value. Other way to describe it - it is an algorithm for finding a needle in a haystack.

For example ([working example here](slides1.ipynb)), we might have the following "haystack" of words:
```python
haystack = ["Hoary Hedgehog", "Gutsy Gibbon", "Oneiric Ocelot", "Precise Pangolin"]
# needle is md5 from one of the words in a haystack
needle = "fd06f6aff94b8f2bade7efde2b949672"
```

If we wanted to find, which word hides under the "needle" `md5`, we would have to iterate over all possible values and check whether md5 of that value is equal to "needle", like this:  

```python
# That is O(n), n = len(haystack)
for word in haystack:
    hashed = md5(word.encode()).hexdigest()
    if hashed == needle:
        print("Aha! Our word is ~~> %s <~~" % word)   
```  

Grover’s algorithm does the same but on "binary" numbers
```python
haystack = [0, 0, 1, 0]
needle = 1

for i, value in enumerate(haystack):
    if value == needle:
        print("Aha! Our 1 is on position %s" % i)
```
