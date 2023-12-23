a=float(input())
r=float(input())
sq=a**2
round=3.1415926*r**2
b=max(sq,round)
if b==sq: print("квадрат",sq)
else: print("круг",round)