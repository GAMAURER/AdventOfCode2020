

la=[]
lu=[]
seen1010=False
f = open("day1input.txt","r")

for line in f.readlines():
    linei=int(line)
    la.append(linei)


for i in la:
    for j in la:
        for k in la:
            if i+j+k==2020:
                print(i,j,k)
                print(i*j*k)
