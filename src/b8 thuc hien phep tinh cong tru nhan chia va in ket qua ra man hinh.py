soThu1, phepTinh, soThu2 = input().split()
try:
    soThu1 =float(soThu1)
    soThu2 = float(soThu2)
    ketQua = None
    if phepTinh == "+":
        ketQua = soThu1 + soThu2
    elif phepTinh == "-":
        ketQua = soThu1 - soThu2
    elif phepTinh == "*":
        ketQua = soThu1 * soThu2
    elif phepTinh == ":":
        if soThu2 == 0:
            print("so bi chia phai khac 0 !")
        else:
            ketQua = soThu1 / soThu2
    if ketQua != None:
        print("{} {} {} = {}".format(soThu1, phepTinh, soThu2, ketQua))
except:
    print("Khong Dung Dinh Danh !")