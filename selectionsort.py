def mysort(x):
    n=len(x)
    y=[]
    while len(y)<n:
        rm=1234567122367263768368372627
        rmi=-1
        for i in range(0,len(x)):
            if x[i]<rm:
                rm=x[i]
                rmi=i
            else:
                pass
        y.append(rm)
        x[rmi]=123456789898892912
    return y
        
            
        
x=[2/3,2,1]
z=mysort(x)
print(z)
