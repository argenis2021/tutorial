#!/usr/bin/python
# Using this line the computer know this is a python executable file

x = 50

def func(x):
    print 'x is', x
    x = 2
    print 'Changed local x to', x

func(x)
print 'x is still', x