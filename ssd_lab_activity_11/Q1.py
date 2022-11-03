import csv
data = []
newData = []
size = 0
with open("lab_11_data.csv", "r") as file:
    reader = csv.reader(file)
    data = list(reader)
    size = len(data)

    for i in range(0, size):
        listToStr = ','.join([str(elem) for elem in data[i]])
        # print(data[i])
        print(listToStr)
        newData.append(data[i][0:-6])

# print(newData)
with open("output1.csv", 'w') as fp:
    writer = csv.writer(fp)

    writer.writerows(newData)


