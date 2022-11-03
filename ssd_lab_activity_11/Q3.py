import csv
data3 = []

funLMD = lambda lst : sum(lst)/len(lst)

with open("output2.csv", "r") as file:
    reader = csv.reader(file)
    data3 = list(reader)
    size3 = len(data3)

    tempList1 = [data3[i][1].replace(',', '') for i in range(1, size3)]
    tempList1 = list(map(float, tempList1))
    tempList2 = [data3[i][2].replace(',', '') for i in range(1, size3)]
    tempList2 = list(map(float, tempList2))
    tempList3 = [data3[i][3].replace(',', '') for i in range(1, size3)]
    tempList3 = list(map(float, tempList3))

    print("-------------------Q3------------------")
    print("Avg Open:", funLMD(tempList1))
    print("Avg High:", funLMD(tempList2))
    print("Avg Low:", funLMD(tempList3))
    print("-------------------END-----------------")

    