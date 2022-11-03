import csv
data2 = []
with open("output1.csv", "r") as file:
    reader = csv.reader(file)
    data2 = list(reader)


def checkChange(dataline):
    # print(dataline)
    # return True
    if float(dataline[6]) < -3:
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




