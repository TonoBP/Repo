def checkio(opacity):
    #CREAMOS A SERIE DE FIBONACCI ATA 5000
    fibo = []
    f0 = 0
    f1 = 1
    f2 = 0
    while f2 < 5000:
        fibo.append(f2)
        f2=f0+f1
        f0=f1
        f1=f2


    age = 0
    units = 10000
    while units != opacity:
        age = age + 1
        if age in fibo:
            units = units - age

        else:
            units = units + 1

    print (age)
checkio(9997)
