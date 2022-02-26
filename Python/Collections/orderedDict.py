from collections import OrderedDict

N=int(input())
orderedDict = OrderedDict()
for i in range(N):
    *item_name, price = input().split()
    item_name = " ".join(item_name) if len(item_name) > 1 else item_name[0]
    
    if item_name in orderedDict:
        orderedDict[item_name] += int(price)
    else:
        orderedDict[item_name] = int(price)

for item_name, net_price in orderedDict.items():
    print(item_name, net_price)


"""9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30"""