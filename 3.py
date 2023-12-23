#даны действительные положительные числа x,y,z.
#Выясниьть, существует ли треугольник с длинами сторон x,y,z
x=int(input())
y=int(input())
z=int(input())

if all([x <=(y+z), y<=(x+z), z<=(y+z)]):
    print("True")
else: print("False")