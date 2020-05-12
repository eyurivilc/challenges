bill = [3, 10, 2, 9]
k = 1
b = 12


# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bTotal = 0
    for item, value in enumerate(bill):
        #print('item{} value={}'.format(item, value))
        if item != k:
            bTotal += value
    
    bActual = bTotal // 2
    overcharged = b - bActual
    print('Bon Appetit') if overcharged == 0 else print(overcharged)
    
    


bonAppetit(bill, k, b)
