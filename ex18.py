#!/usr/bin/env python
# coding=utf-8
#This one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
#OK, that *args is actually pointless, we can just do this
def print_tow_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

#this just takes one argument
def print_one(arg1):
    print "arg1: %r" % arg1

#this one takes no argument
def print_none():
    print "I got nothing."


print_two("kengus", "benfree")
print_tow_again("kengus", "benfree")
print_one("First!!")
print_none()

