giaTri1 = input("Nhap so thu nhat: ") #nhap gia tri thu nhat
giaTri2 = input("Nhap so thu hai: ") #nhap gia tri thu hai

try: # khoi lenh khong phat sinh loi
    so1 = int(giaTri1) # ep kieu gia tri 1
    so2 = int(giaTri2) # ep kieu gia tri 2
    sum = so1 + so2 # tong hai so nguyen 
    print("tong hai so nguyen vua nhap la: ", sum) # in ra man hinh tong hai so nguyen

except: #khoi lenh co the phat sinh loi input
    print("Dinh dang dau vao khong hop le ! hay nhap lai") 