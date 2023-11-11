a = float(input("he so a: "))
b = float(input("he so b: "))
if a ==0:
    if b ==0:
        print("Phương trình vô nghiệm")
    else:
        print("phương trình có vô số nghiệm")  
else:
    x = -b/a
    print("Phương trình có nghiệm duy nhất là: ", x)    