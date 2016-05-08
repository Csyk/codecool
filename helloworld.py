import sys

def Hello(name=" World"):
    print("Hello " + name + "!")
try:
    for x in sys.argv[1:]:
        name = x
    Hello(name)
except:
    Hello ()

