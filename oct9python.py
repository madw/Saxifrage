import sys

USAGE = "Usage: ./find.py word filename [filename]*"

def fail(msg):
    print >> sys.stderr, USAGE
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
        print >> sys.stderr, "Could not open file:", filename
        continue

    for line in file_pointer:
        if word in line:
            print filename
            break