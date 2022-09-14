import operator
#이름:이선주, 학번:2021041042

traintuplelist=[('토마스',5),('헨리',8),('에드워드',9),('에밀리',5),
                ('토마스',4),('헨리',7),('토마스',3),('에밀리',8),
                ('퍼시',5),('고든',13)]
traindic, trainlist={},[]
tmptup=None
totalrank,currentrank=1,1

if __name__=="__main__":
    for tmptup in traintuplelist:
        tname=tmptup[0]
        tweight=tmptup[1]
        if tname in traindic:
            traindic[tname]+=tweight


        else:
            traindic[tname]=tweight

    print('기차 수송량 목록 ==>', traintuplelist)
    print('-----------------------')
    trainlist=sorted(traindic.items(), key=operator.itemgetter(1),reverse=True)

    print("%20s" % '기차\t총 수송량\t순위')
    print('-----------------------')
    print("%10s" % trainlist[0][0],'\t',trainlist[0][1],'\t\t', currentrank)
    for i in range(1, len(trainlist)):
        totalrank+=1
        if trainlist[i][1]==trainlist[i-1][1]:
            pass
        else:
            currentrank=totalrank
        print("%10s"  % trainlist[i][0],'\t' ,trainlist[i][1],'\t\t',currentrank)
                     
            
            
