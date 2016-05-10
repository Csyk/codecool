command = input("Please specify a command [list, add, mark, archive]: ")

if (command == "list"):
    fo = open("todo.txt", "r")
    print (fo.read())

if (command == "add"):
    fo = open("todo.txt", "a")
    fo.write(('\n') + "[ ]" + input())

if (command == "mark"):
    fo = open("todo.txt", "r")
    print (fo.read().count("[ ]" + input()))
    #fo.seek(k) #odaugrik
