# Caesar Project
<br>

## 프로젝트 개요
> **파이썬으로 시저 암호를 구현함**
> * caesar : 소문자/대문자 알파벳, 숫자, 공백으로 이루어진 caeser 
> * caesarASCII : ASCII code로 이루어진 caeser
----------


<br>

# dist 파일 실행 설명(배포판)

- 실행 파일 이름 : dist
    - caesar를 실행할 경우

    ```
    1. dist 압축 풀기
    2. dist/caesar/caesar.exe 실행
    ```


    - caesarASCII를 실행할 경우
    
    ```
    1. dist 압축 풀기
    2. dist/caesarASCII/caesarASCII.exe 실행
    ```
----------

<br>

# 코드 설명
### `caesar.py`

1. import 
    ``` python
    import os
    os.system("pause")
    ```

    * 명령 프롬프트 결과 실행 후 화면 대기 상태 유지

<br>

2. 초기값 
    ``` python
    # 알파벳 소문자 초기화 리스트
    inAlp1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    #알파벳 대문자 초기화 리스트
    inAlp2 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    #숫자 초기화 리스트
    inNum = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    #암호 이동 칸 수 초기값
    cryp = 3

    #암호화 값 초기 리스트
    resultList = []

    #복호화 값 초기 리스트
    resultList2 = []
    ```

<br>

3. main
    ``` python

    # main 함수 정의
    def caesar():
    
        # input 배열 정의
        x = list(input("입력 값 : "))

        # 암호화 함수 실행
        Encrpytion(x)

        # 복호화 함수 실행
        Decrpytion()

        # 대기
        os.system("pause")
    
    # main 함수 실행
    caesar()
    ```

<br>

4. 암호화

    ``` python
    # 암호화 함수 정의
    def Encrpytion(inData):

        # input 길이
        for i in range(len(inData)):

            # 조건의 맞는 배열 암호화
            if inData[i] in inAlp1:

                # 리스트 순회
                result = inAlp1[(inAlp1.index(inData[i]) + cryp) % 26]

                # 암호화 결과 append
                resultList.append(result)

            # 조건의 맞는 배열 암호화
            elif inData[i] in inAlp2:

                # 리스트 순회
                result = inAlp2[(inAlp2.index(inData[i]) + cryp) % 26]

                # 암호화 결과 append
                resultList.append(result)

            # 조건의 맞는 배열 암호화
            elif inData[i] == ' ':

                # 암호화 결과 append
                resultList.append(' ')

            # 조건의 맞는 배열 암호화
            else:

                # 리스트 순회
                result = inNum[((inNum.index(inData[i]) + cryp) % 10)]

                # 암호화 결과 append
                resultList.append(result)

        # 최종 암호화 결과 print
        print("암호화 : " + ''.join(resultList))

    ```

<br>

    
5. 복호화
    ``` python

    # 복호화 함수 정의
    def Decrpytion():

        # 암호화 길이
        for i in range(len(resultList)):

            # 조건의 맞는 배열 복호화
            if resultList[i] in inAlp1:

                # 리스트 순회
                result = inAlp1[(inAlp1.index(resultList[i]) - cryp) % 26]

                # 복호화 결과 append
                resultList2.append(result)

            # 조건의 맞는 배열 복호화
            elif resultList[i] in inAlp2:

                # 리스트 순회
                result = inAlp2[(inAlp2.index(resultList[i]) - cryp) % 26]

                # 복호화 결과 append
                resultList2.append(result)

            # 조건의 맞는 배열 복호화
            elif resultList[i] == ' ':

                # 복호화 결과 append
                resultList2.append(' ')

            # 조건의 맞는 배열 복호화
            else:

                # 리스트 순회
                result = inNum[((inNum.index(resultList[i]) - cryp) % 10)]

                # 복호화 결과 append
                resultList2.append(result)

        # 최종 복호화 결과 print
        print("복호화 : " + ''.join(resultList2))
    ```

<br>

### `caesarASCII.py`

1. import 
    ``` python
    import os
    os.system("pause")
    ```

    * 명령 프롬프트 결과 실행 후 화면 대기 상태 유지

<br>

2. 초기값
    ``` python
    #암호 이동 칸 수 초기값
    cryp = 3

    #암호화 값 초기 리스트
    resultList = []

    #복호화 값 초기 리스트
    resultList2 = []
    ```

<br>

3. main
    ``` python

    # main 함수 정의
    def caesarASCII():

        # input 배열 정의
        x = list(input("입력 값 : "))

        # 암호화 함수 실행
        EncryptionASCII(x)

        # 복호화 함수 실행
        DecryptionASCII()

        # 대기
        os.system("pause")

    # main 함수 실행
    caesarASCII()
    ```

<br>

4. 암호화
    ``` python

    # 암호화 함수 정의
    def EncryptionASCII(inData):

        # input 길이
        for i in range(len(inData)):

            # 조건의 맞는 ASCII 시저암호화
            resultNum = (ord(inData[i]) % 128) + cryp

            # ASCII값 반환
            result = chr(resultNum)

            # ASCII 결과 append
            resultList.append(result)
        
        # 최종 암호화 결과 print
        print("암호화 : " + ''.join(resultList))
    ```

<br>

5. 복호화
    ``` python

    # 복호화 함수 정의
    def DecryptionASCII():

        # 암호화 길이
        for i in range(len(resultList)):

            # 조건의 맞는 ASCII 시저암호화
            resultNum = (ord(resultList[i]) % 128) - cryp

            # ASCII값 반환
            result = chr(resultNum)

            # ASCII 결과 append
            resultList2.append(result)

        # 최종 복호화 결과 print
        print("복호화 : " + ''.join(resultList2))

    ```

----------
