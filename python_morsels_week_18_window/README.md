CHALLENGE Email (7/30/2018):

Hi there,

This week I'd like you to write a function returns "windows" of items from a given list. Your function should takes a
list and a number n and return a new list of tuples, each containing "windows" of n consecutive items. That is, each
tuple should contain the current item and the n-1 items after it.

Here are some examples:
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> window(numbers, 2)
[(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
>>> window(numbers, 3)
[(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
>>> window(numbers, 4)
[(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]
Your window function should return an empty list if the given n is 0. It should also be able to accept strings, tuples
and other sequences.

This week's problem is challenging. I recommend solving the base problem before either of the bonuses this week.

As a bonus, make sure your function accepts any iterables, not just sequences. ✔️

For example your function should accept iterators and other lazy iterables:
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> squares = (n**2 for n in numbers)
>>> window(squares, 3)
[(1, 4, 9), (4, 9, 16), (9, 16, 25), (16, 25, 36)]

For a second bonus, make sure your function returns an iterator instead of a list. ✔️
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> next(window(numbers, 3))
(1, 2, 3)

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named
window.py next to the test file. To run the tests you'll run "python test_window.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus,
you'll want to comment out the noted lines of code in the tests file to test them properly.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOLUTIONS email (8/1/2018):

Hey!

If you haven't attempted to solve window yet, close this email and go do that now before reading on. If you have
attempted solving window, read on...

This week you needed to make a function that takes a list and returns a list of tuples, each containing "windows" of n
consecutive items.

Let's take a look at a solution that uses indexes to look up the next n items for each item in the iterable.
def window(sequence, n):
    """Return list of tuples of items in given list and next n-1 items."""
    items = []
    for i in range(len(sequence)):
        if i+n <= len(sequence):
            items.append(tuple(sequence[i:i+n]))
    return items
Note that we're converting the slice we're getting into a tuple here.  We're doing this so we get a consistent return
value.  Slicing a list gives us a list and slicing a string gives us a string.  If we always want a tuple returned, we
need to convert the slice to a tuple.

Also note that we're using range(len(sequence)) here.  You should pretty much never use range(len(...)) (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzIyNjc0NTY0NCIsInVybCI6Imh0dHA6Ly90cmV5aHVubmVyLmNvbS8yMDE2LzA0L2hvdy10by1sb29wLXdpdGgtaW5kZXhlcy1pbi1weXRob24vP19fcz1wNTIyZ2hreXVucHc2a292cWpxcyJ9)
in your code. This is an exceptional case because we don't need tho actual item here, but a slice that involves the
item index.

Notice that we're ignoring the case of n=0. Currently we return a list full of empty tuples in this case (one for each
item in our list). There's no test for this case so this behavior can be ignored for now (maybe we'll define what
should happen for this case in a later exercise).

This solution passes all our tests.

We could have instead solved this problem this way:
def window(sequence, n):
    """Return list of tuples of items in given list and next n-1 items."""
    sequences = [sequence[i:] for i in range(n)]
    return zip(*sequences)
Here we're making n copies of the given sequence, each with 1 fewer item than the one before it.  Then we zip them
together and return their items.  If you're unfamiliar with zip, you might want to read the article I linked above.

Let's try the first bonus.

Bonus #1
For the first bonus we needed to make sure our function accepted any iterable, not just sequences.

To do this we need to keep track of the n-1 items before ours and only start adding items to our returned list once
we're at the n-th item.

This solution works:
def window(iterable, n):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = current + (item,)
        else:
            current = current[1:] + (item,)
        if len(current) == n:
            items.append(current)
    return items
Here we're using the variable current to keep track of a tuple that will have an item added to the end until we have n
items in the tuple.  Once there are n items we'll make a new tuple with the oldest item removed and our new item added
to the end.

The reason we have that awkward looking (item,) thing is that we need to make a single item tuple to add it to our
existing tuple and make a new one.

We could instead make a new tuple by unpacking the current tuple into a new tuple and adding item to the end, like
this:
def window(iterable, n):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        if len(current) < n:
            current = (*current, item)
        else:
            current = (*current[1:], item)
        if len(current) == n:
            items.append(current)
    return items
We're using * to unpack one tuple into another tuple.  This particular ability of the * operator was added in Python
3.5.

You might have tried to collapse that if statement into a single slice that took the last n-1 items in the current
tuple and then added a new one, like this:
def window(iterable, n):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        current = (*current[-(n-1):], item)
        if len(current) == n:
            items.append(current)
    return items
This fails our tests though.  The reason this fails our tests is that when n is 1, -(n-1) will be 0, and if we slice
from 0 onward, we'll get the entire tuple back.  Meaning whenever n is 1, our tuples will expand in size instead of
always only having n items in them.

We could get around this problem by subtracting from the length of the current tuple to make a positive.
def window(iterable, n):
    """Return list of tuples of items in given iterable and next n-1 items."""
    items = []
    current = ()
    for item in iterable:
        current = (*current[len(current)-n+1:], item)
        if len(current) == n:
            items.append(current)
    return items
Okay let's try the second bonus now.

Bonus #2
For the second bonus, we needed to return an iterator from our function.  If you're unclear on what iterators are,
here's an article (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzIyNjc0NTY0NCIsInVybCI6Imh0dHA6Ly90cmV5aHVubmVyLmNvbS8yMDE2LzEyL3B5dGhvbi1pdGVyYXRvci1wcm90b2NvbC1ob3ctZm9yLWxvb3BzLXdvcmsvP19fcz1wNTIyZ2hreXVucHc2a292cWpxcyJ9)
I've written about them.

We can do that by turning our function into a generator function, which will cause a generator to be returned when our
function is called (generators are iterators).
def window(iterable, n):
    """Yield tuples including iterable item and the next n-1 items."""
    current = ()
    for item in iterable:
        current = (*current[len(current)-n+1:], item)
        if len(current) == n:
            yield current
The yield keyword makes our function into a generator function.  It's sort of magical and that fact is a little
confusing, but it's true.  The presence of a yield statement magically makes our function a fundamentally different
thing.

You might have noticed that we've been treating our "current" tuple sort of like it's a queue.  Queues are ordered
structures which can have their oldest item removed from the beginning and the newest item added to the end.

Python's collections module has a deque (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzIyNjc0NTY0NCIsInVybCI6Imh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGlicmFyeS9jb2xsZWN0aW9ucy5odG1sP19fcz1wNTIyZ2hreXVucHc2a292cWpxcyNjb2xsZWN0aW9ucy5kZXF1ZSJ9)
which is a double-ended queue:
from collections import deque

def window(iterable, n):
    """Yield tuples including iterable item and the next n-1 items."""
    current = deque(maxlen=n)
    for item in iterable:
        current.append(item)
        if len(current) == n:
            yield tuple(current)
We've made deque object with a maximum length of n.  When we append something to the end of our deque, if it is already
length n, it will remove the last inserted item from the beginning to make room for the new one.

Note that we have a check for the length of our deque inside our loop, but we really only need that check for the first
n-1 items. Our loop would be faster if we didn't have to do this check for every item.

We could prepopulate our deque like this:
from collections import deque

def window(iterable, n):
    iterator = iter(iterable)
    current = deque(maxlen=n)
    for _ in range(n):
        current.append(next(iterator))
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)
Here we're getting an iterator from our iterable and dealing with that iterator in the rest of our function.  This is
important because iterators are consumed as you work with them.  After we've taken each item out of our iterator, it
will be removed from it permanently.

We're relying on the single-use behavior of iterators here by removing the first n items and then taking the rest of
the items using our for loop.

This might seem a bit uglier, but our "for" loop at the end doesn't have to do as much work this way.

We could instead populate the deque using islice (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzIyNjc0NTY0NCIsInVybCI6Imh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGlicmFyeS9pdGVydG9vbHMuaHRtbD9fX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMjaXRlcnRvb2xzLmlzbGljZSJ9):
from collections import deque
from itertools import islice

def window(iterable, n):
    iterator = iter(iterable)
    current = deque(islice(iterator, n), maxlen=n)
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)
The islice utility will grab the next n items in our iterator, which is exactly what we were doing manually in our
"for" loop before.

If you're not familiar with collections.deque and itertools.islice, I'd highly recommend looking into both of them.
They're very useful helpers.

That deque/islice solution is my preferred solution. But I'd like to show another solution to this problem that is very
clever and possibly a little confusing:
from itertools import islice, tee

def window(iterable, n):
    """Yield tuples including iterable item and the next n-1 items."""
    iterators = [
        islice(iterator, i, None)
        for i, iterator in enumerate(tee(iterable, n))
    ]
    return zip(*iterators)
If you haven't seen tee (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzIyNjc0NTY0NCIsInVybCI6Imh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGlicmFyeS9pdGVydG9vbHMuaHRtbD9fX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMjaXRlcnRvb2xzLnRlZSJ9)
before, this is likely quite confusing. It's a little tricky to explain what tee does.

Essentially we're getting n iterators over our iterable, which appear to move independently because they cache the
values they receive from the given iterable.

The for loop we've written is removing 0 items from the first iterator, 1 item from the next, and so on until it
removes n-1 items from the n-th iterator. Then we zip the iterators together to get our answer.  This use of zip is
very similar to the one we used above. We're essentially working with slices of these iterables here instead of slices
of sequences.

I find these solutions with tee to be overly clever. I rarely find that the itertools.tee utility improves code
clarity, so I usually recommend against using tee.

My preferred solution to this problem is this one:
from collections import deque
from itertools import islice

def window(iterable, n):
    iterator = iter(iterable)
    current = deque(islice(iterator, n), maxlen=n)
    yield tuple(current)
    for item in iterator:
        current.append(item)
        yield tuple(current)
I hope you learned something from this somewhat lengthy adventure.