def ReadFile():
    file=open('input.txt','r')
    line=file.readline()
    line=line.split('=')
    equa=[c for c in line[1]]
    line=line[0].split("+")
    line=[[s[i] for i in range(len(s))] for s in line]
    line=[["" for _ in range(len(equa)-len(s))]+s for s in line]
    file.close()
    return [['c'+str(i) for i in reversed(range(len(equa)))]]+line+[equa]+[['c'+str(i) if(i==0) else 'c'+str(len(equa)-i) for i in range(len(equa))]]

def SaveFile(output):
    file=open('output.txt','w')
    s=[]
    for c in output:
        if(len(c)==1): s.append(c)
    for c in sorted(s): file.write(output[c])
    file.close()
