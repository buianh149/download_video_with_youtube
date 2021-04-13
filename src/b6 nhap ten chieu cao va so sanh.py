tenBan1 = input("nhap ten ban thu nhat: ")
#print("Name 1: " + tenBan1)
tenBan2 = input("nhap ten ban thu hai: ")
#print("Name 2: " + tenBan2)
chieuCaoBan1 = input("nhap chieu cao ban thu nhat: ")
chieuCaoBan2 = input("nhap chieu cao ban thu hai: ")

try:
    chieuCaoBan1 = float(chieuCaoBan1)
    #print("Height 1: " + chieuCaoBan1)
    chieuCaoBan2 = float(chieuCaoBan2)
    #print("Height 2: " + chieuCaoBan2)
    if chieuCaoBan1 <= 0 or chieuCaoBan2 <= 0:
        print("chieu cao phai lon hon 0!")
        if chieuCaoBan1 == chieuCaoBan2:
            print(tenBan1 + " cao bang " + tenBan2)
        elif chieuCaoBan1 > chieuCaoBan2:
            print(tenBan1 + " cao hon " + tenBan2)
        else:
            print(tenBan1 + "thap hon" + tenBan2)
except:
    print("Dinh dang dau vao khong dung !!!")
