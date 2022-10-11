"""
2-(1)

Eratos(a[n], n)
    a[1]<-0;
        for (i<-2;i*i<=n;i<=i+1) do
            if(a[i]!=0) then
            for (j<-i*i ;j<n; j<-j+i) do
                a[i*j] <- 0;

end Eratos()

"""



"""
2-2
"""

def SofEratos(a, n):
    a[1]=0
    for i in range(2, (i<n//2)+1):
        if(a[i]!=0):
            for j in range(i*i, j<n, i):
                a[i*j] = 0
    return a


        

    
        
            

