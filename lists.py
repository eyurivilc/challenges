""" input
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print 
"""

""" output
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1] 
"""



if __name__ == '__main__':
    N = int(input())
    myList = {}

    for c in range(N):
        command, *line = input().split()
        values = list(map(int, line))
        myList[command] = values
    
    newList = []
    for cmd, val in myList.items():
        if cmd == 'insert':
            newList.insert(val[0], val[1])
        elif cmd == 'remove':
            newList.remove(val[0])
        elif cmd == 'append':
            newList.append(val[0])
        elif cmd == 'sort':
            newList.sort()
        elif cmd == 'pop':
            newList.pop()
        elif cmd == 'reverse':
            newList.reverse()
        elif cmd == 'print':
            print(newList)
        
        newList = []
        if cmd == 'print':
            print(myList)
        else:
            if count(val) == 2:
                myList.cmd(val[0])
            elif count(val) == 1:
                myList.cmd(val[0])
            else:
                myList.cmd()
