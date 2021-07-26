def remove_parathesis(sign):
    index=0
    for _ in range(sign.count('(')):
        index=sign.index('(',index)
        if sign[index-1]=='-':
            while index!=sign.index(')',index):
                if sign[index]=='+':sign[index]='-'
                elif sign[index]=='-':sign[index]='+'
                index=index+1
    index=0
    while sign.count('(')!=0:
        index=sign.index('(',index)
        sign.pop(index)
        index=sign.index(')',index)
        sign.pop(index)
 
    
def readfile():
    sign="-+*/="
    file=open('input.txt','r')
    line=file.readline()
    file.close()

    result=[]
    sign_order=['+']
    s=0
    max_len=0
    for i in range(len(line)):
        if line[i] in sign and line[i-1]!=")":
            sign_order.append(line[i])
            result.append([c for c in line[s:i]])
            if i-s>max_len: max_len=i-s
            s=i+1
        elif line[i]=="(":
            sign_order.append(line[i])
            s=i+1
        elif line[i]==")":
            sign_order.append(line[i])
            result.append([c for c in line[s:i]])
            sign_order.append(line[i+1])
            s=i+2
    
    sign_order.pop()
    if len(line[s:])>max_len: max_len=len(line[s:])
    result=result+[[c for c in line[s:]]]
    result=[['' for _ in range(max_len-len(s))]+s for s in result]
    remove_parathesis(sign_order)
    return [['c'+str(i) for i in reversed(range(max_len))]]+result+[['c'+str(i) if(i==0) else 'c'+str(max_len-i) for i in range(max_len)]],sign_order

def savefile(output):
    file=open('output.txt','w')
    tmp=sorted(output)
    for c in tmp:
        if(len(c)==1): file.write(str(output[c]))
    file.close()

