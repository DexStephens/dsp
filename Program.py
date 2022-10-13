from Customer import Customer

# Program start
# Variable representing my queue of customers
custLine = []

# Dictionary<string,int>
custDict = {}

# put 100 customers into the queue
for cust in range(0, 100):
    custLine.append(Customer())

# do the loopy stuff
for custorder in range(0, len(custLine)):
    if custLine[custorder].customer_name in custDict.keys():
        custDict[custLine[custorder].customer_name] += custLine[custorder].order.burger_count
    else:
        custDict[custLine[custorder].customer_name] = custLine[custorder].order.burger_count

listSortedCustomers = sorted(custDict.items(), key=lambda x: x[1], reverse=True)

for finalCust in range(0, len(listSortedCustomers)):
    print(f'{listSortedCustomers[finalCust][0]}: {listSortedCustomers[finalCust][1]}')

