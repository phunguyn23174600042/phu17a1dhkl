import math
a = float(input("do dai canh a: "))
b = float(input("do dai canh b: "))
c = float(input("do dai cẠNH c: "))
p=(a+b+c)/2
S= math.sqrt(p*(p-a)*(p-b)*(p-c))
print("dien tich tam giac tren la: ",S)