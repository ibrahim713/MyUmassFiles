import stdio
import sys


# Returns the domain type of the given URL.
def domain_type(URL):
    ...


# Test client [DO NOT EDIT]. Reads a URL as command-line argument and writes
# its domain type.
def _main():
    URL = sys.argv[1]
    stdio.writeln(domain_type(URL))

if __name__ == '__main__':
    _main()
