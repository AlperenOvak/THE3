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
        #func=eval("d_"+str(degree))
        P=["".join(eval("d_"+str(degree))(P)[i]) for i in range(len(eval("d_"+str(degree))(P)))]
    for i in range(len(I)):
        escape=0
        a=I[i].find(P[0][0])
        if a!=(-1):
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
    return (False,False)
def pattern_search(P, I):
    a,result=False,False
    degree=0
    while a==False and degree<360:
        a,result=browse(P,I,degree)
        degree+=90
    return(result)

    
I = ["tuz<abcz",
     "tuzAabcz",
     ">xxAY#at", 
     "uzyXAAr.", 
     "r,lAXxio",  
     "z#a!yabc", 
     "yaAy?zyY"]
P1 = ["AXA", "XAY"]
print(pattern_search(P1,I))  

