
def readfile():
    sign="+-*/()"
    file=open('input.txt','r')
    line=file.readline()
    file.close()
    
    # line=line.split('=')
    # equa=[c for c in line[1]]
    # line=line[0].split("+")
    # line=[[s[i] for i in range(len(s))] for s in line]
    # line=[["" for _ in range(len(equa)-len(s))]+s for s in line]
    result=[]
    sign_order=[]
    s=0
    for i in range(len(line)):
        if line[i] in sign:
            sign_order.append(line[i])
            result.append([c for c in line[s:i]])
            s=i+1

    return result+[sign_order]

    # return [['c'+str(i) for i in reversed(range(len(equa)))]]+line+[equa]+[['c'+str(i) if(i==0) else 'c'+str(len(equa)-i) for i in range(len(equa))]]

def savefile(output):
    file=open('output.txt','w')
    for c in output:
        if(len(c)==1): file.write(str(output[c]))
    file.close()

s=readfile()
print(s)