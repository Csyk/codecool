command = input("Please specify a command [list, add, mark, archive]: ")

if (command == "list"):
    fo = open("todo.txt", "r")
    print (fo.read())

if (command == "add"):
    fo = open("todo.txt", "a")
    fo.write(('\n') + "[ ]" + input())

if (command == "mark"):
    fo = open("todo.txt", "r")
    mylist = fo.readlines()
    print("\n".join(mylist))
    y = str(input())
    for i in range(len(mylist)):
        x = "[ ]" + y
        if x == mylist[i]:
            mylist[i] = "[x]" + y
            print(mylist[i])
