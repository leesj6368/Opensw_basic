#이름:이선주 학번:2021041042
i,k,heartNum=0,0,0 
numStr,ch,heartStr="","",""



numStr=input("숫자를 여러개 입력하세요 : ") #
print("")

i=0
ch=numStr[i] 

while True :
    heartNum=int(ch)
    heartStr=""
    for k in range(0,heartNum) :
        heartStr += "\u2665"
        k+=1
    print(heartStr)


    i+=1
    if (i>len(numStr)-1) :
        break
    ch=numStr[i]
