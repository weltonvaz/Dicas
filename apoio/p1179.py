
for p in range(0,5):
    print("par[%d] = %d" %(p,par[p]))
    del par[p]
for i in range(0,5):
    print("impar[%d] = %d" %(i,impar[i]))
    del impar[i]
for i in range(0,len(impar)):
    print("impar[%d] = %d" %(i,impar[i]))
for p in range(0,len(par)):
    print("par[%d] = %d" %(p,par[p]))

for p in range(0,len(par)):
    print("par[%d] = %d" %(p,par[p]))
