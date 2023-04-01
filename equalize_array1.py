
def equalize_array(arr):
    array_amount = {}
    for item in arr:
        if item in array_amount:
            array_amount[item] += 1
        else:
            array_amount[item] = 1
    print(array_amount)
    more_quantity = max(array_amount, key=array_amount.get)
    return len([item for item in arr if item != more_quantity])

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
print (equalize_array(ar))
