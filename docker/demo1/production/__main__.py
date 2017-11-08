import sys

from . import should_pass

should_pass = should_pass * 5

if len(sys.argv) == 2:
    should_pass = should_pass + int(sys.argv[1])

from . import print_hello

print_hello.run(should_pass)