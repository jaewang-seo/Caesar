# ASCII
import os

cryp = 3
resultList = []
resultList2 = []

def EncryptionASCII(inData):
    for i in range(len(inData)):
        resultNum = (ord(inData[i]) % 128) + cryp
        result = chr(resultNum)
        resultList.append(result)
    print("암호화 : " + ''.join(resultList))

def DecryptionASCII():
    for i in range(len(resultList)):
        resultNum = (ord(resultList[i]) % 128) - cryp
        result = chr(resultNum)
        resultList2.append(result)
    print("복호화 : " + ''.join(resultList2))
    
def caesarASCII():
    x = list(input("입력 값 : "))
    EncryptionASCII(x)
    DecryptionASCII()
    os.system("pause")

caesarASCII()