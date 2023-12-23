x=int(input(""))

n=int(input(""))

fir_str=1

sec_str=0

th_str=0

zn=1
ch=1
for i in range(n+1):

    ch *= x

    zn *=(i + 1)

    znam=x*(x+i)


    fir_str *= (x - i * n)

    sec_str+=1/znam

    th_str+=ch/zn

print(fir_str,sec_str,th_str)
