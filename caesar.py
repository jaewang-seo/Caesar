import os

inAlp1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
inAlp2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
inNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
cryp = 3
resultList = []
resultList2 = []

def Encrpytion(inData):
    for i in range(len(inData)):
        if inData[i] in inAlp1:
            result = inAlp1[(inAlp1.index(inData[i]) + cryp) % 26]
            resultList.append(result)
        elif inData[i] in inAlp2:
            result = inAlp2[(inAlp2.index(inData[i]) + cryp) % 26]
            resultList.append(result)
        elif inData[i] == ' ':
            resultList.append(' ')
        else:
            result = inNum[((inNum.index(inData[i]) + cryp) % 10)]
            resultList.append(result)
    print("암호화 : " + ''.join(resultList))

def Decrpytion():
    for i in range(len(resultList)):
        if resultList[i] in inAlp1:
            result = inAlp1[(inAlp1.index(resultList[i]) - cryp) % 26]
            resultList2.append(result)
        elif resultList[i] in inAlp2:
            result = inAlp2[(inAlp2.index(resultList[i]) - cryp) % 26]
            resultList2.append(result)
        elif resultList[i] == ' ':
            resultList2.append(' ')
        else:
            result = inNum[((inNum.index(resultList[i]) - cryp) % 10)]
            resultList2.append(result)
    print("복호화 : " + ''.join(resultList2))

def caesar():
    x = list(input("입력 값 : "))
    Encrpytion(x)
    Decrpytion()
    os.system("pause")
caesar()