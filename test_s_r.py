#!/usr/bin/python

# First Example
s = 'spam'
# "repr" returns a printable representation of an object,
# which means the quote marks will also be printed.
print(repr(s))
# 'spam'
# "str" returns a nicely printable representation of an
# object, which means the quote marks are not included.
print(str(s))
# spam

# Second Example.
x = "example"
print ("My %r" %x)
# My 'example'
# Note that the original double quotes now appear as single quotes.
print ("My %s" %x)
# My example

# Third Example.
x = 'xxx'
withR = ("Prints with quotes: %r" %x)
withS = ("Prints without quotes: %s" %x)
print(withR)
# Prints with quotes: 'xxx'
print(withS)
# Prints without quotes: xxx
