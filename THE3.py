def d_0(patt): return patt    
def d_90(patt):
    rotate_pattern=[[patt[m][n] for m in range(len(patt)-1,-1,-1)] for n in range(len(patt[0]))]
    return rotate_pattern
def d_180(patt):
    rotate_pattern=[[patt[m][n] for m in range(len(patt)-1,-1,-1)] for n in range(len(patt[0])-1,-1,-1)]
    return rotate_pattern
def d_270(patt):
    rotate_pattern=[[patt[m][n] for m in range(len(patt))] for n in range(len(patt[0])-1,-1,-1)]
    return rotate_pattern
def browse(P,I,degree):
    if degree!=0:
        P=["".join(eval("d_"+str(degree))(P)[i]) for i in range(len(eval("d_"+str(degree))(P)))]
    I2=I[:]        
    for i in range(len(I)):
        a=I[i].find(P[0][0])
        while a!=(-1):
            escape=0
            for j in range(len(P[0])):
                for k in range(len(P)):
                    try:
                        loc=I[i+k][a+j]
                    except IndexError:
                        escape+=1
                        break
                    if P[k][j]!=loc:
                        escape+=1
                        break
                if escape!=0:break
            if escape==0:return(True,(i,a,degree))
            I2[i]=I2[i][:a]+"c"+I2[(a+1):] if "c"==P[0][0] else I2[i][:a]+"d"+I2[i][(a+1):]
            a=I2[i].find(P[0][0])
    return (False,False)
def pattern_search(P, I):
    a,result=False,False
    degree=0
    while a==False and degree<360:
        a,result=browse(P,I,degree)
        degree+=90
    return(result)

    
I = ["CAA<abcA",
     "AXYLYXAt", 
     "YAXXAAX.", 
     "r,lAXYIo",  
     "z#aYAXbc", 
     "yaAAXAyY"]
P1 = ["AXA", "XAY"]
print(pattern_search(P1,I))  

