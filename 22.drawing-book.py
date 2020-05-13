
n1 = 6
p1 = 2
n2 = 5
p2 = 4
n = 7
p = 3

def pageCount(n, p):
    book = [pages for pages in range(n+1)]
    if n > 2 and n%2 == 0:
        book.append(0)
        
    steps = 0
    mid = n // 2

    if p <= mid:
        for i in range(0,mid+1,2):
            if book[i] == p or book[i+1] == p:
                break
            steps += 1
    else:
        for j in range(len(book)-1,mid,-2):
            if book[j] == p or book[j-1] == p:
                break
            steps += 1
    

    print(steps)




pageCount(n, p)
