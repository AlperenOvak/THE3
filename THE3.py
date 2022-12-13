def d_0(patt):
    return patt
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
    escape=0
    #print(degree)
    if degree!=0:
        func=eval("d_"+str(degree))
        P=["".join(func(P)[i]) for i in range(len(func(P)))]
    for i in range(len(I)):
        a=I[i].find(P[0][0])
        if a!=(-1):
            for j in range(len(P[0])):
                for k in range(len(P)):
                    if P[k][j]!=I[i+k][a+j]:
                        escape+=1
                        break
                if escape!=0:
                    break
            if escape==0:
                return(True,(i,a,degree))
    return (False,False)
def pattern_search(P, I):
    a,result=False,False
    degree=0
    while a==False and degree<360:
        a,result=browse(P,I,degree)
        degree+=90
    return(result)

    
I = ["tuz<abcd", 
     ">#sAY#at", 
     "uzyXAAr.", 
     "r,lAXxio", 
     "z#a!yabc", 
     "yazy?zya"]
P1 = ["AXA", "XAZ"]
print(pattern_search(P1,I))
#m = ["1234",
#     "2334",
#     "5434"]
#print(d_180(m))

"""escape=0
    P=["".join(d_270(P)[i]) for i in range(len(d_270(P)))]
    for i in range(len(I)):
        a=I[i].find(P[0][0])
        if a!=(-1):
            for j in range(len(P[0])):
                for k in range(len(I)):
                    if P[k][j]!=I[i+k][a+j]:
                        escape+=1
                        break
                    else:
                        return(True)
                if escape==1:
                    break"""
            