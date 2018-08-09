CHALLENGE Email (4/9/2018 @ 7:00 AM):

Hey! 👋

When solving this week's exercise, make sure to hold off on searching directly for the answer in Google/StackOverflow.
🚫🔍 This is a fairly general exercise and there are a number of answers to it. I'd like you to struggle to come to an
answer or two (or five?) on your own.

I want you to write a function that accepts a string and returns a mapping (a dictionary or dictionary-like structure)
that has words as the keys and the number of times each word was seen as the values.

Your function should work like this:
>>> count_words("oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}
>>> count_words("don't stop believing")
{"don't": 1, 'stop': 1, 'believing': 1}

As a bonus, make sure your function works well with mixed case words:
>>> count_words("Oh what a day what a lovely day")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}

For even more of a bonus try to get your function to ignore punctuation outside of words:
>>> count_words("Oh what a day, what a lovely day!")
{'oh': 1, 'what': 2, 'a': 2, 'day': 2, 'lovely': 1}


Automated tests for this week's exercise can be found here. You'll need to write your function in a module named
count.py next to the test file. To run the tests you'll run "python test_count.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus,
you'll want to comment out a line or two of code to test them properly. You'll see those noted in the test file.

You'll receive some answers and links to resources explaining ways to solve this exercise within a few days. Don't peek
at the answers before attempting to solve this on your own. 😄


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOLUTIONS email (4/11/2018 @ 7:00 AM):

Hey friend!

If you haven't attempted to solve count_words yet, close this email and go do that now before reading on. If you have
attempted solving count_words, read on...

We're going to talk about solving this by manually building up a dictionary first. Then we'll discuss some helper
utilities we could have used instead. After that we'll discuss the two bonus solutions.

If we solve this using a dictionary. We'll need to handle two cases:
The word is not yet in the dictionary. We need to add it with a value of 1 in this case.
The word is already in the dictionary. We need to increment its value in this case.
Here's one possible answer using a dictionary:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return count

Notice that we use the string split method to get words. The split method splits on any number of consecutive white
space (including spaces, linebreaks, tabs, etc) by default.

The if statement checks for the presence of a key corresponding to each word. The if statement could have been written
without an else instead:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        if word not in count:
            count[word] = 0
        count[word] += 1
    return count

Dictionaries also have a get method that can be used to lookup the value for a given key or get a specific default
value if the key isn't in the dictionary. This could be used instead of that if statement:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        count[word] = count.get(word, 0) + 1
    return count

Dictionaries also have a setdefault method that can be used to add a key-value pair to the dictionary with a given
default value if the key isn't in the dictionary:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = {}
    for word in string.split():
        count.setdefault(word, 0)
        count[word] += 1
    return count

There are even more ways this could have been solved with dictionaries than these ones I've mentioned so far, but I'm
going to stop talking about the various ways to solve this with plain old dictionaries and discuss other ways we can
solve this. Let's talk about the collections module.

There's a defaultdict class in the collections module that creates a dictionary-like object that includes a recipe for
calculating default values to set for keys that are accessed before they are put in the dictionary. We can use
defaultdict(int) to solve this particular exercise:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    count = defaultdict(int)
    for word in string.split():
        count[word] += 1
    return count

That's pretty neat. We essentially don't need any of the defaulting in our dictionary because defaultdict does that for
us. We can make this even simpler though. The Counter object will do all of the work we're doing for us:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(string.split())

Counter objects are essentially a dictionary-like object specifically meant for counting the number of times things are
seen and storing the things as keys and the times seen as values. You can think of it as essentially a set that counts
the number of times it sees each thing, a multi-set of sorts.

Okay so that was a lot. If you're still interested in the various ways to solve this problem and you'd like to dive
through history slightly, you might want to check out an article I wrote on specifically this problem.

Now let's talk about the bonus problems...

Bonus #1
If we want to ignore the case of words, we could normalize the case by lowercasing all the words:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(string.lower().split())

This has the side effect of losing information about the cases of the words we're counting, but it's hard to solve this
problem without losing that information.

Bonus #2
Okay now what if we want to ignore punctuation? This one was a little harder.

We could strip punctuation characters from the ends of words after we loop through them:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    words = []
    for word in string.lower().split():
        words.append(word.strip(',;.!?"()'))
    return Counter(words)
This will require us to list all punctuation characters we'd like to strip from the ends of words. You could reach for
string.punctation in the standard library, but that won't solve this problem.

In fact this particular answer doesn't pass our tests currently because our tests call this function with an inverted
question mark (¿) currently.

We could take a different approach. Instead of splitting our string by whitespace, we could use a regular expression to
search for consecutive letters and symbols that should be considered as part of words:
def count_words(string):
    """Return the number of times each word occurs in the string."""
    return Counter(re.findall(r"[\w'-]+", string.lower()))

We're lowercasing the string first and then using findall to find word-like letters (\w includes letters, digits, and
underscore and we've included apostrophe and dash) one or more times consecutively (that's what + means).

Note that this allows things like "--", "-", and "yes-" to be seen as words. If we wanted to get more accurate, we
could use word breaks in our regular expression. Instead of this:
r"[\w'-]+"
We could do this:
r"\b[\w'-]+\b"
Writing this using a rawstring (with the r prefix) is important because those \b would be interpreted as backspace
characters otherwise.

Note that this is a bit easier to read than if we explicitly required the ends of our word to be "word characters",
because we'd need to special-case a single-letter word:
r"(\w[\w'-]*\w|\w)"
There's always a balance with regular expressions between being as accurate as possible and being just good enough for
the use cases we actually care about.

Did you learn anything from these solutions? Wait a day and then try solving these again using something you learned.
