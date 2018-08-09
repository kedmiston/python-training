CHALLENGE Email (7/16/2018):

Hello!

This week we're going to practice normalizing CSV files.  Write a program fix_csv.py that turns a pipe-delimited file
into a CSV file. I'll explain how it should work by example.

Your original file will look like this:
Reading|Make|Model|Type|Value
Reading 0|Toyota|Previa|distance|19.83942
Reading 1|Dodge|Intrepid|distance|31.28257

You'll then run your script by typing this at the command line:
$ python fix_csv.py cars-original.csv cars.csv

Note: "$" is not typed; that is simply the beginning of the prompt.

Your fixed file should then look like this:
Reading,Make,Model,Type,Value
Reading 0,Toyota,Previa,distance,19.83942
Reading 1,Dodge,Intrepid,distance,31.28257
Hint: you'll likely want to use the csv module (in the Python standard library) for this because you'll find yourself
struggling pretty quickly without it.


For the first bonus, I want you to allow the input delimiter and quote character to be optionally specified. ✔️

For example any of these should work (all specify input delimiter as pipe and the last two additionally specifies the
quote character as single quote):
$ python fix_csv.py --in-delimiter="|" cars.csv cars-fixed.csv
$ python fix_csv.py cars.csv cars-fixed.csv --in-delimiter="|"
$ python fix_csv.py --in-delimiter="|" --in-quote="'" cars.csv cars-fixed.csv
$ python fix_csv.py --in-quote="'" --in-delimiter="|" cars.csv cars-fixed.csv
This bonus will require looking into parsing command-line arguments with Python. There are some standard library
modules that can help you out with this. There are 3 different solutions in the standard library actually, but only
one I'd recommend.

For the second bonus, automatically detect the delimiter if an in-delimiter value isn't supplied (don't assume it's
pipe and quote, figure it out). ✔️

The second bonus is a bit trickier and I don't expect it to work correctly for all files.  You'll likely want to
consult the csv module documentation if you're going to attempt it.

Automated tests for this week's exercise can be found here. You'll need to write your function in a module named
fix_csv.py next to the test file. To run the tests you'll run "python test_fix_csv.py" and check the output for "OK".
You'll see that there are some "expected failures" (or "unexpected successes" maybe). If you'd like to do the bonus,
you'll want to comment out the noted lines of code in the tests file to test them properly.


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

SOLUTIONS email (7/18/2018):

Hey! 👋

If you haven't attempted to solve fix_csv.py yet, close this email and go do that now before reading on. If you have
attempted solving fix_csv.py, read on...

This fix_csv.py program is supposed to accept the name of an existing pipe-delimited file and the name of a new
comma-delimited file.

Here's one solution:
import sys


old_filename = sys.argv[1]
new_filename = sys.argv[2]

old_file = open(old_filename)
rows = [
    line.split('|')
    for line in old_file.read().splitlines()
]

new_file = open(new_filename, mode='wt', newline='\r\n')
print("\n".join(
    ",".join(row)
    for row in rows
), file=new_file)
old_file.close()
new_file.close()

This solution doesn't pass our tests though.  One reason is that it doesn't handle quotes when delimiters are in the
output data.  We could use the csv module to fix that.
import csv
import sys


old_filename = sys.argv[1]
new_filename = sys.argv[2]

with open(old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    rows = [line for line in reader]

with open(new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)

Notice that we've changed a couple different things here.

One big change is that we're using csv.reader and csv.writer to handle parsing our delimited data files for us.
Notice that the csv module works for any delimited data files, not just comma-delimited files.

Another change is that we're using "with" blocks here to ensure our files are always automatically closed when we're
done with them.

This still doesn't pass our tests though.  The reason is that our script currently accepts more than 2 arguments and
simply ignores all arguments after the first two:
$ python fix_csv.py in_file.psv out_file.csv another_arg and_another
We can fix this by slicing our arguments and unpacking them into exactly two variables.

Instead of this:
old_filename = sys.argv[1]
new_filename = sys.argv[2]
We'll do this:
old_filename, new_filename = sys.argv[1:]
This is a lazy way of ensuring an exception is raised (even though it's not a very friendly one) unless exactly 2
arguments are given (we're using multiple assignment here).

We could also improve this line:
    rows = [line for line in reader]
Whenever you see a list comprehension that loops over something and doesn't filter anything or change any item but just
makes a list, you can replace it with the list constructor:
    rows = list(reader)
The list constructor loops over whatever you give it and makes a new list.

If we wanted to, we could collapse this code a bit by writing one line for both the reader and the writer:
import csv
import sys


old_filename, new_filename = sys.argv[1:]

with open(old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))

with open(new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)

Notice in both of these open calls we've been specifying newline as an empty string.  The reason that the CSV module
writes \r\n line endings to our file automatically, but Python will automatically take all LF endings (\n) and convert
them to CRLF endings (\r\n) on Windows systems.  So when writing CSV files in Python 3, using newline='' is
recommended.  In Python 2, you'll want to use mode 'wb' instead for similar reasons.

The newline='' in the reading open isn't necessary because the CSV module handles either \r\n and \n as line endings,
but I think it's nice to be consistent when opening files that are meant to represent CRLF-ended delimited data.

Another thing I'll note about the csv reader and writer objects is that the writer's writerows method takes an iterable
and the reader object is an iterable. So if we nested our with statements, we could actually write directly while
reading:
import csv
import sys


old_filename, new_filename = sys.argv[1:]

with open(old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter='|')
    with open(new_filename, mode='wt', newline='') as new_file:
        csv.writer(new_file).writerows(reader)
This has a big benefit but also a downside.

The big benefit is that this allows us to efficiently process very large delimited files because we're processing our
files line-by-line here. Every line that is read immediately results in one line that is written (because reader reads
lazily line by line and writerows loops lazily over the iterable it's given as it's writing).

The downside is that if we provided the same filename for both input and output, we'd get some weird results because
we'd be writing to a file as we were reading it which is often a bad idea.

So I'm going continue doing things the copy-into-list-and-use-two-with-blocks way that we did above. If you'd prefer to
write as you read, you could do pass reader directly into the writer's writerows method instead though.

One more improvement we could make before jumping into the first bonus is to make the command-line functionality of our
script a bit more robust.

We can use argparse from the standard library to do that:
from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    rows = list(csv.reader(old_file, delimiter='|'))

with open(args.new_filename, mode='wt', newline='') as new_file:
    csv.writer(new_file).writerows(rows)

The argparse library makes our command-line script have a friendly interface that requires the correct number of
arguments, shows usage information when -h or --help flags are given, and shows helpful error messages when incorrect
command-line arguments are provided.

Using argparse will also make the first bonus easier.

Before we get to the first bonus, note that there are two other command-line parsing tools in the standard library that
you may hear about, but both are focused on option parsing (for flags like -i and --in-quote) and neither handles
positional arguments from the command-line. See the section why aren't getopt and optparse enough from PEP 389 (the PEP
that created argparse years ago).

Bonus #1
For this bonus we had to accept optional arguments for the delimiter and quote character of the input data file.

We can modify our program to accept those arguments like this:
from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    quotechar = '"'
    delimiter = '|'
    if args.delim:
        delimiter = args.delim
    if args.quote:
        quotechar = args.quote
    reader = csv.reader(old_file, delimiter=delimiter, quotechar=quotechar)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)

We've added two more arguments to our argument parser and both are optional (the default for arguments specified with
--).

Note that we've added quite a bit of code to handle these new arguments when reading our input file.  The default
values for these arguments (if they're unspecified) is None.  So we're defaulting them to | and " and only changing
those default values if they're "truthy" (None is falsey so evaluates to False in that if condition).  You can think
of truthiness as non-emptiness.

To make things easier we can set the default values for these arguments when we add the arguments:
from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim', default='|')
parser.add_argument('--in-quote', dest='quote', default='"')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    reader = csv.reader(old_file, delimiter=args.delim, quotechar=args.quote)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)

This removes all the conditional checking and exceptional cases from our code.

Okay let's try the second bonus.

Bonus #2
This bonus was a bit tricky.  The objective was to automatically detect (or attempt to detect) the format of the input
file.

To do this, we can use the csv module's Sniffer class:
from argparse import ArgumentParser
import csv


parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
    arguments = {}
    if args.delim:
        arguments['delimiter'] = args.delim
    if args.quote:
        arguments['quotechar'] = args.quote
    if not args.delim and not args.quote:
        arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
        old_file.seek(0)
    reader = csv.reader(old_file, **arguments)
    rows = list(reader)

with open(args.new_filename, mode='wt', newline='') as new_file:
    writer = csv.writer(new_file)
    writer.writerows(rows)

Our code here is a bit complex.  If a delimiter and/or quote character are specified, we provide keyword arguments for
those to our csv reader object.  If neither is specified, then we use the csv Sniffer object to detect them.

Note that we're sniffing our entire csv file and then seeking back to the beginning of the file so that we can start
reading it again.  Files are iterators which means they're stateful: they keep track of where we are in them as we loop
over them.

If you're unfamiliar with that ** syntax, you might want to read the article I've written on keyword arguments in
Python.

I hope you found this exercise to be good practice for creating command-line programs and working with delimited data!