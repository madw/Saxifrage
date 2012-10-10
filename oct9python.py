#!/usr/bin/env python

# The "import" statement finds modules (whatever those are!) and defines names
# in a namespace (whatever that is!):                                                                          
#                                                                                                              
#   http://docs.python.org/reference/simple_stmts.html#the-import-statement                                    
#                                                                                                              
# The "sys" module provides things related (apparently) to the interpreter
# (whatever that is!):                                                                                         
#                                                                                                              
#   http://docs.python.org/library/sys.html

#this opens the sys library
import sys

USAGE = "Usage: ./find.py word filename [filename]*"

def fail(msg):
    # print chevron: the first expression after the >> must evaluate to a “file-like” object
    print >> sys.stderr, USAGE
    # sys = library, file, ...?
    print >> sys.stderr, msg
    sys.exit()

try:
    word = sys.argv[1]
except:
    fail("Please provide a word to find.")

filenames = sys.argv[2:]
if not filenames:
    fail("Please enter at least one filename.")

for filename in filenames:
    try:
        file_pointer = open(filename)
    except IOError:
        # print chevron: the first expression after the >> must evaluate to a “file-like” object
        print >> sys.stderr, "Could not open file:", filename
        continue

    for line in file_pointer:
        if word in line:
            print filename
            break