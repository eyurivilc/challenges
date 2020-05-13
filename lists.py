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

""" command=insert and values ['0', '5']
values => [0, 5]
command=insert and values ['1', '10']
values => [1, 10]
command=insert and values ['0', '6']
values => [0, 6]
command=print and values []
values => []
command=remove and values ['6']
values => [6]
command=append and values ['9']
values => [9]
command=append and values ['1']
values => [1]
command=sort and values []
values => []
command=print and values []
values => []
command=pop and values []
values => []
command=reverse and values []
values => []

command=print and values []
values => []
{'insert': [0, 6], 'print': [], 'remove': [6], 'append': [1], 'sort': [], 'pop': [], 'reverse': []} """



if __name__ == '__main__':
    N = int(input())
    myList = {}

    for c in range(N):
        command, *line = input().split()
        print(f"command={command} and values {line}")
        values = list(map(int, line))
        print(f"values => {values}")
        myList[command] = values
    
    print(myList)
