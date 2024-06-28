def postmansort(x):
    y=[]
    z=[]
    a=[]
    b=[]
    mm=0
    rm=162676367
    for i in range(0,len(x)):
        if rm>x[i]:
            rm=x[i]
        else:
            pass
    for i in x:
        a.append(i-rm+1)
    for i in range(0,len(a)):
        if mm<a[i]:
            mm=a[i]
        else:
            pass
    for j in range(0,mm+1):
        y.append(0)
    for i in a: 
        y[i]=i
    for i in y:
        if i>0:
            z.append(i)
    for i in z:
        b.append(i+rm-1)
    return b
x=[1,2,-3]
print(postmansort(x))
