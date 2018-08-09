CHALLENGE Email (8/6/2018):

Hey!

This week we're revisiting the interleave problem we solved a few weeks ago and extending it further. For an extra
challenge, try to solve this problem without peeking at your previous solutions.

I want you to write a function that accepts two iterables and returns a new iterable with each of the given items
"interleaved" (item 0 from iterable 1, then item 0 from iterable 2, then item 1 from iterable 1, and so on).

Here's an example (which returns lists):
>>> interleave([1, 2, 3, 4], [5, 6, 7, 8])
[1, 5, 2, 6, 3, 7, 4, 8]
>>> nums = [1, 2, 3, 4]
>>> interleave(nums, (n**2 for n in nums))
[1, 1, 2, 4, 3, 9, 4, 16]
Note that any iterable can be accepted by this function: lists, generators, sets, or anything else you can iterate over.

As a bonus, return an iterator (for example a generator) from your interleave function instead of a list. ✔️
>>> interleave([1, 2, 3, 4], [5, 6, 7, 8])
<generator object interleave at 0x7f6174c18b48>
>>> list(interleave([1, 2, 3, 4], [5, 6, 7, 8]))
[1, 5, 2, 6, 3, 7, 4, 8]

This should allow your interleave function to accept infinitely long iterables (or other lazy iterables).

Here's another bonus to do after you've made your interleave function return a lazy iterable: make your interleave
function accept any number of arguments. ✔️

For example:
>>> interleave([1, 2, 3], [4, 5, 6], [7, 8, 9])
[1, 4, 7, 2, 5, 8, 3, 6, 9]

If you do that bonus too, here's a much more challenging bonus: allow your interleave function to work with arguments
of different length. ✔️

Any short iterables should be skipped over once exhausted. For example:
>>> interleave([1, 2, 3], [4, 5, 6, 7, 8])
[1, 4, 2, 5, 3, 6, 7, 8]
>>> interleave([1, 2, 3], [4, 5], [6, 7, 8, 9])
[1, 4, 6, 2, 5, 7, 3, 8, 9]

I would recommend attempting the initial exercise before any of the bonuses and then solving the bonuses in order. This
one could take quite a while if you're not careful so don't get too hung up on attempting to solve any of the bonuses,
especially the last one. Make sure to time box yourself!

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named
interleave2.py next to the test file. To run the tests you'll run "python test_interleave2.py" and check the output
for "OK". You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the
bonus, you'll want to comment out the noted lines of code in the tests file to test them properly.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOLUTIONS email (8/8/2018):

Hey!

If you haven't attempted to solve the interleave part 2 problem yet, close this email and go do that now before reading
on. If you have attempted solving interleave part 2, read on...

If we want to loop over two lists at the same time, you might think to use indexes to look up corresponding items as
you loop:
def interleave(iterable1, iterable2):
    """Return iterable of one item at a time from each list."""
    interleaved = []
    for i, item in enumerate(iterable1):
        interleaved.append(item)
        interleaved.append(iterable2[i])
    return interleaved
This works for lists but it won't work for all types of iterables, so it doesn't pass our tests.

If we pass in a generator our function won't work:
>>> nums = [1, 2, 3, 4]
>>> interleave(nums, (n**2 for n in nums))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 6, in interleave
TypeError: 'generator' object is not subscriptable
Python has another utility we can use to loop over multiple iterables at the same time: the built-in zip function.
def interleave(iterable1, iterable2):
    interleaved = []
    for item1, item2 in zip(iterable1, iterable2):
        interleaved.append(item1)
        interleaved.append(item2)
    return interleaved
If you're not familiar with zip and its usage for looping over multiple iterables at once, you might want to read (or
re-read) this article on looping in Python (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHA6Ly90cmV5aHVubmVyLmNvbS8yMDE2LzA0L2hvdy10by1sb29wLXdpdGgtaW5kZXhlcy1pbi1weXRob24vP19fcz1wNTIyZ2hreXVucHc2a292cWpxcyJ9)
with indexes.

So zip gives us back tuples of items as we loop over it.  Notice that we're unpacking the items into item1 and item2
and then appending each to the new list.

This almost looks like something we could convert to a list comprehension... but not quite.

To convert this to a list comprehension, we need just a single append statement in our loop. Let's restructure our code
to include a nested loop and a single append::
def interleave(iterable1, iterable2):
    interleaved = []
    for items in zip(iterable1, iterable2):
        for item in items:
            interleaved.append(item)
    return interleaved
With our code written in this format we can copy-paste our way into a list comprehension:
def interleave(iterable1, iterable2):
    return [
        item
        for pair in zip(iterable1, iterable2)
        for item in pair
    ]
Notice that this list comprehension has two for clauses.  This isn't two list comprehensions nested inside each other,
it's one list comprehension with nested for loops in it.  Also notice the order of the for clauses.  That order is
important and it's hard to remember unless you copy-paste your way into a comprehension from for loops.  If you need a
refresher on list comprehensions, read this article on list comprehensions (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHA6Ly90cmV5aHVubmVyLmNvbS8yMDE1LzEyL3B5dGhvbi1saXN0LWNvbXByZWhlbnNpb25zLW5vdy1pbi1jb2xvci8_X19zPXA1MjJnaGt5dW5wdzZrb3ZxanFzIn0)
or watch this talk on comprehensions (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9NV9jSkljZ003cndcdTAwMjZfX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMifQ).

If you'd a whole bunch of experience with comprehensions, try out my PyCon 2018 tutorial (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9XzZVMVhveHl5QllcdTAwMjZfX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMifQ)
on list comprehensions and generator expressions.

Bonus #1
Let's attempt the first bonus now. In the first bonus we were asked to return an iterator (a lazy iterable) from our
function instead of a list.

We could make a lazy iterable instead of a list by turning our list comprehension into a generator expression. We can
do this by replacing the square brackets with parentheses:
def interleave(iterable1, iterable2):
    return (
        item
        for pair in zip(iterable1, iterable2)
        for item in pair
    )
This is one way to make a generator. Another way to make a generator is to make a generator function.

The easiest way to do that is to take our first working solution (with two appends) and replace the two appends with
yield statements:
def interleave(iterable1, iterable2):
    for item1, item2 in zip(iterable1, iterable2):
        yield item1
        yield item2
We don't need a list in that example because our generator function will return a generator that will yield new items
as it's looped over.

Which of these two solutions you prefer may depend on whether you find generator functions scary and whether you find
the generator expression syntax readable. I like both of them.

Let's try the second bonus now.

Bonus #2
For the second bonus exercise we're supposed to allow our function to accept any number of arguments. If we're using
the zip function this is deceptively easy:
def interleave(*iterables):
    return (
        item
        for items in zip(*iterables)
        for item in items
    )
The first * captures all arguments passed to interleave and packs them into a tuple.  The second * unpacks those values
into separate arguments passed to the zip function. Those * (star operators) are often tricky for folks new to Python.

If you're looking for a generator function solution, you could use "yield from" to yield each of the items individually
while looping over the zip object. This is the equivalent of putting a for loop within a for loop and yielding each
item individually.
def interleave(*iterables):
    for items in zip(*iterables):
        yield from items
I really like both of these two solutions.

We could avoid using loops or generator expressions for this shallow "flattening" operation on the zip return value by
using the itertools.chain utility instead.
from itertools import chain

def interleave(*iterables):
    return chain.from_iterable(zip(*iterables))
The chain utility loops over the zip object we give it and then loops over the iterables in that object and gives us
each item individually. It's an iterator that is returned to us.

Note that we're not doing "chain(*zip(*iterables))" here, but "chain.from_iterable(zip(*iterables))".  The chain
function would work but the chain.from_iterable (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGlicmFyeS9pdGVydG9vbHMuaHRtbD9fX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMjaXRlcnRvb2xzLmNoYWluLmZyb21faXRlcmFibGUifQ)
function doesn't require unpacking the whole zip object into arguments
before looping over its items.

Let's take a look at the third bonus now.  This one is a bit trickier than the first two bonuses.

Bonus #3
The third bonus exercise requires us accept iterables of different lengths.  Our interleave function should keep
filling in items in order, removing short iterables from the interleaving once they're used up.

One way we could do this is to use itertools.zip_longest (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGlicmFyeS9pdGVydG9vbHMuaHRtbD9fX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMjaXRlcnRvb2xzLnppcF9sb25nZXN0In0)
with a fillvalue that we can ensure we skip over:
from itertools import zip_longest

def interleave(*iterables):
    sentinel = object()
    for items in zip_longest(*iterables, fillvalue=sentinel):
        for item in items:
            if item is not sentinel:
                yield item

A sentinel value is a unique value that can be used to identify special items. The zip_longest function fills these
sentinel values into our zip object when iterables of different lengths are zipped together and we'll need to remove
them to get a properly interleaved iterable.

Note that zip_longest defaults to a fill value of None. That works okay, but if you have None values in your iterable,
you won't be able to distinguish the None values added by zip_longest from your own None values. Using a unique
sentinel object as your fill value fixes this problem because you're the only one who will ever reference your unique
object. We're using object() here because the "is" check on a new object() will always return False unless we see the
exact same object (which means we're looking at one of the filled-values added by zip_longest).

We could use a generator expression instead of a generator function:
from itertools import zip_longest

def interleave(*iterables):
    sentinel = object()
    return (
        item
        for items in zip_longest(*iterables, fillvalue=sentinel)
        for item in items
        if item is not sentinel
    )
There's a lot going on in this generator expression and I might prefer our generator function instead, but both are
reasonable solutions.

We could also solve this bonus without writing any for loops or generator expressions at all. If we combine
chain.from_iterable and zip_longest with the built-in filter function, we can zip our iterables together, flatten them
one level with chain, and then filter out the sentinel values with filter:
from itertools import chain, zip_longest

def interleave(*iterables):
    sentinel = object()
    def not_sentinel(item): return item is not sentinel
    zipped = zip_longest(*iterables, fillvalue=sentinel)
    flattened = chain.from_iterable(zipped)
    return filter(not_sentinel, flattened)
I wouldn't recommend this solution though. That filter function doesn't improve readability much. The zipped and
flattened variables describe what we're doing, but they don't make our code much more descriptive.

We could keep using chain but use a generator expression instead of filter:
from itertools import chain, zip_longest

def interleave(*iterables):
    sentinel = object()
    zipped = zip_longest(*iterables, fillvalue=sentinel)
    flattened = chain.from_iterable(zipped)
    return (x for x in flattened if x is not sentinel)
This one doesn't seem so bad. The shape of our code doesn't necessarily make it clear that we're looping, but we can
see the steps we take along the way. Personally I still prefer the generator function or large generator expression
solutions over this.

You may have actually noticed that there's a solution for this problem in the itertools documentation (in the recipes
(http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHBzOi8vZG9jcy5weXRob24ub3JnLzMvbGlicmFyeS9pdGVydG9vbHMuaHRtbD9fX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMjaXRlcnRvb2xzLXJlY2lwZXMifQ)
section). It looks like this:
from itertools import cycle, islice

def interleave(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    num_active = len(iterables)
    iterators = cycle(iter(it) for it in iterables)
    while num_active:
        try:
            for iterator in iterators:
                yield next(iterator)
        except StopIteration:
            # Remove the iterator we just exhausted from the cycle.
            num_active -= 1
            iterators = cycle(islice(iterators, num_active))
I find this solution confusing and weird, but there's something important in here that we haven't tried yet. This
solution is manually grabbing an iterator from each iterable and then grabbing one item from each iterator in order,
removing iterators from our iterators "cycle" until they're all exhausted.

Here's a much simpler way to do the same thing:
def interleave(*iterables):
    iterators = [iter(i) for i in iterables]
    while iterators:
        for iterator in list(iterators):
            try:
                yield next(iterator)
            except StopIteration:
                iterators.remove(iterator)
Here we're making a list of iterators (one for each of our iterables in order).

Then as long as there are iterators left, we loop over each iterator in order, attempt to grab yield the next item from
each, and remove each iterator once it has no more items.

Notice that we're copying our list of iterators before we loop over it (with "list(iterators)"). We're doing this
because if we loop over iterators and remove an item from it, we'll skip the next iterator which will cause things to
be yielded out of order.

Without that list conversion, we'd get bugs like this:
>>> list(interleave([1], [2, 3], [4, 5], [6]))
[1, 2, 4, 6, 5, 3]
That [5, 3] at the end should be [3, 5].

If you're not sure what's going on with the list-copying situation, try calling remove on items in a simple list of
numbers while iterating over it. If you're unfamiliar with iterators and what's going on here, you should read this
article on iterators and the iterator protocol (http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHA6Ly90cmV5aHVubmVyLmNvbS8yMDE2LzEyL3B5dGhvbi1pdGVyYXRvci1wcm90b2NvbC1ob3ctZm9yLWxvb3BzLXdvcmsvP19fcz1wNTIyZ2hreXVucHc2a292cWpxcyJ9)
or watch this talk on iterators
(http://t.dripemail2.com/c/eyJhY2NvdW50X2lkIjoiMzk0NTg2MCIsImRlbGl2ZXJ5X2lkIjoiMzI3NzcxODM0MSIsInVybCI6Imh0dHBzOi8vd3d3LnlvdXR1YmUuY29tL3dhdGNoP3Y9VjJQa2tNUzJBY2tcdTAwMjZfX3M9cDUyMmdoa3l1bnB3NmtvdnFqcXMifQ).

I prefer both this solution and the generator function and generator expression solutions.