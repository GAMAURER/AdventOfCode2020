

la=[]
lu=[]
seen1010=False
f = open("day1input.txt","r")

for line in f.readlines():
    linei=int(line)
    if linei<1010:
        lu.append(linei)
    elif linei>1010:
        la.append(linei)
    else:
        if seen1010:
            print(1010*1010)
        else:
            seen1010=True

for i in la:
    for j in lu:
        if i+j==2020:
            print(i,j)
            print(i*j)
