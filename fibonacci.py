fibo = []
f0 = 0
f1 = 1
f2 = 0
while f2 < 5000:
    fibo.append(f2)
    f2=f0+f1
    f0=f1
    f1=f2
print (fibo)
