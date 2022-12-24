def d_0(patt):   return [[patt[m][n] for n in range(len(patt[0]))] for m in range(len(patt))]    #return 0 degree
def d_90(patt):  return [[patt[m][n] for m in range(len(patt)-1,-1,-1)] for n in range(len(patt[0]))] #return 90 degree
def d_180(patt): return [[patt[m][n] for n in range(len(patt[0])-1,-1,-1)] for m in range(len(patt)-1,-1,-1)] #return 180 degree
def d_270(patt): return [[patt[m][n] for m in range(len(patt))] for n in range(len(patt[0])-1,-1,-1)] #return 270 degree
def browse(P,I,degree):
    if degree!=0:
        P=["".join(eval("d_"+str(degree))(P)[i]) for i in range(len(eval("d_"+str(degree))(P)))] #call returning function
    I2=I[:]      
    for i in range(len(I)-len(P)+1):
        a=I[i][:1-len(P[0])].find(P[0][0])  #find the first letter of pattern in initial line
        while a!=(-1):
            escape=0
            for j in range(len(P[0])):
                for k in range(len(P)):                 
                    if P[k][j]!=I[i+k][a+j]: #check if it is pattern
                        escape+=1
                        break   
                if escape!=0:break
            if escape==0:return(True,(i,a,degree)) #We find
            I2[i]=I2[i][:a]+"c"+I2[i][(a+1):] if "c"!=P[0][0] else I2[i][:a]+"d"+I2[i][(a+1):] # if the first finding is not our case then change it to chack if there are some other letters
            a=I2[i][:1-len(P[0])].find(P[0][0])
    return (False,False)  #If there is no result, return False
def pattern_search(P, I):
    a,result,degree=False,False,0
    while a==False and degree<360:
        a,result=browse(P,I,degree)
        degree+=90 #increase degree by 90 degree
    return(result)

    

