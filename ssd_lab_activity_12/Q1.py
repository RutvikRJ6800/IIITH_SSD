ptr = 0
wholeFile = []
with open("readings.txt", "r") as file:
    wholeFile = file.readlines()
    # print(wholeFile)

nextMatrix = list(list())
nextTime = ""

# get matrix
def getNextMatrix():
    global nextTime
    global nextMatrix
    global ptr
    global wholeFile
    nextMatrix.clear()
    if(ptr!=0):
        ptr += 3
    for i in range(ptr,ptr+42):
        if(i>= len(wholeFile)):
            break
        lineString = wholeFile[i]
        line = lineString.split('\t')
        line = line[1:-1]
        nextMatrix.append(line)
    nextTime = wholeFile[ptr+20].split('\t')[0]
    ptr = ptr + 42



# main function execution
firstLegFound = False
firstLegIdx = tuple()
firstLegTime = 0
secondLegFound = False
secondLegIdx = tuple()
secondLegTime = 0

while((not firstLegFound) or (not secondLegFound)):
    getNextMatrix() #stores next matrix to nextMatrix global array
    # 
    if not firstLegFound:
        for i in range(42):
            if firstLegFound:
                break
            for j in range(25):
                if int(nextMatrix[i][j]) != 0:
                    # print("True****i:",i,",j:",j)
                    firstLegFound = True
                    firstLegIdx = (i,j)
                    firstLegTime = nextTime
                    break

    # first leg found now searching second leg            
    elif not secondLegFound:
        leftLimit = firstLegIdx[1]-4
        rightLimit = firstLegIdx[1]+4
        bottomLimit = firstLegIdx[0]-4
        if leftLimit<0:
            leftLimit = 0
        if bottomLimit<0:
            bottomLimit = 0
        if rightLimit>=24:
            rightLimit = 24

        for i in range(bottomLimit):
            if secondLegFound:
                break
            for j in range(leftLimit,rightLimit):
                if int(nextMatrix[i][j]) != 0:
                    # print("True**in second**i:",i,",j:",j)
                    secondLegFound = True
                    secondLegIdx = (i,j)
                    secondLegTime = nextTime
                    break

if(firstLegFound and secondLegFound):
    # print leg and time details
    # print("both leg found")
    # print("first leg Time: ",firstLegTime)
    # print("first Leg Inx: ",firstLegIdx)
    # print("second leg Time: ",secondLegTime)
    # print("second Leg Inx: ",secondLegIdx)
    print("Both Leg found. Details are as below...")
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    stride = abs(secondLegIdx[0] - firstLegIdx[0])
    print("stride length:", stride)

    startTime = firstLegTime
    TimeList1 =firstLegTime.split(".")[0].split(":")
    TimeList2 =secondLegTime.split(".")[0].split(":")

    time1 = int(TimeList1[0])*3600 + int(TimeList1[1])*60 + int(TimeList1[2])
    time2 = int(TimeList2[0])*3600 + int(TimeList2[1])*60 + int(TimeList2[2])

    velocity = stride / (time2 - time1)

    print("velocity: ", velocity)
    Cadence = 60 // (time2-time1)
    print("Cadence: ", Cadence)
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")

else:
    print("Sorry, No same leg found two times.")