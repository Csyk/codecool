import sys

def Hello(name=" World"):
    print("Hello " + name + "!")

for x in sys.argv[1:]:
    name = x
Hello(name)
