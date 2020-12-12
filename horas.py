def time_converter(time):
    #replace this for solution
    c = time.split(":")
    if int(c[0])<12:
        c[0]=int(c[0])+12
        c=(str(c[0])+":"+c[1]+" p.m.")

    elif int(c[0])==12:
        c=(c[0]+":"+c[1]+" p.m.")

    else:
        c=(c[0]+":"+c[1]+" a.m.")
time_converter("12:47")
