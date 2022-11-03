import csv
data = []
newData = []
size = 0
with open("inp.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)
    size = len(data)

    for i in range(0, size):
        listToStr = ','.join([str(elem) for elem in data[i]])
        # print(data[i])
        print(listToStr)
        newData.append(data[i][0:-6])

print(newData)
with open("output1.csv", 'w') as fp:
    writer = csv.writer(fp)

    writer.writerows(newData)




# Q2
data2 = []
with open("output1.csv", "r") as file:
    reader = csv.reader(file)
    data2 = list(reader)


def checkChange(dataline):
    # print(dataline)
    # return True
    if float(dataline[-1]) < -3:
        return False
    else:
        return True


header = data2[0]
filtered2 = filter(checkChange, data2[1:])

# print(newData2)
with open("output2.csv", 'w') as fp:
    writer = csv.writer(fp)

    writer.writerow(header)
    writer.writerows(filtered2)


# Q3
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

    
# Q4
data4 = []
print("-------------------Q4------------------")
inputAlpha = input("Enter char btwn A-Z :- ")
print("-------------------END-----------------")


with open("output2.csv", "r") as file:
    reader = csv.reader(file)
    data4 = list(reader)
    size4 = len(data4)

    for i in range(0, size4):
        # print(data4[i][0])
        if(data4[i][0][0] == inputAlpha):    
            listToStr = ' '.join([str(elem) for elem in data4[i]])
            # print(data[i])
            print(listToStr)


# Q5
with open("stock_output.txt", "w") as finalP:
    for i in range(0, size4):
        # print(data4[i][0])
   
        listToStr = ','.join([str(elem) for elem in data4[i]])
        # print(data[i])
        listToStr = listToStr + '\n'
        finalP.write(listToStr)