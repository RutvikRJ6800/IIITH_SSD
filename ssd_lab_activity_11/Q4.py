import csv
data4 = []
inputAlpha = input("Enter char btwn A-Z :- ")


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

with open("stock_output.txt", "w") as finalP:
    for i in range(0, size4):
        # print(data4[i][0])
   
        listToStr = ','.join([str(elem) for elem in data4[i]])
        # print(data[i])
        listToStr = listToStr + '\n'
        finalP.write(listToStr)


