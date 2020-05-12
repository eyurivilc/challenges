n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]


def sockMerchant(n, ar):
    pairs = 0
    uniqueValues = set(ar)
    amountValues = []

    for value in uniqueValues:
        amount = ar.count(value)
        amountValues.append(amount)
    
    for x in amountValues:
        if x >= 2:
            pairs  += x//2 

    print(pairs)

sockMerchant(n, ar)
