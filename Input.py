def readfile():
    sign="-+*/()="
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
    max_len=0
    for i in range(len(line)):
        if line[i] in sign:
            sign_order.append(line[i])
            result.append([c for c in line[s:i]])
            if i-s>max_len: max_len=i-s
            s=i+1
    sign_order.pop()
    result=result+[[c for c in line[s:]]]
    result=[['' for _ in range(max_len-len(s))]+s for s in result]

    return [['c'+str(i) for i in reversed(range(max_len))]]+result+[sign_order]+[['c'+str(i) if(i==0) else 'c'+str(max_len-i) for i in range(max_len)]]

def savefile(output):
    file=open('output.txt','w')
    for c in output:
        if(len(c)==1): file.write(str(output[c]))
    file.close()

s=readfile()
print(s)