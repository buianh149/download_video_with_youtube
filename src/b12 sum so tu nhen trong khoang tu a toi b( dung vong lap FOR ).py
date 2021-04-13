
try:
    a, b = map(int, input().split())
    print("Nhap so thu nhat: {}\nNhap so thu hai: {}".format(a, b))
    if a > b:
        print("nhap lai so, so thu nhat khong duoc lon hon so thu hai")
    else: 
        sum = 0
        for i in range(a, b+1):
            sum +=i
        print(sum)
except:
    print("dinh dang k hop le")