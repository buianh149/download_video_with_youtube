try:
    with open('bai10.1.input', 'r') as fileInp:
        dongDauTien = fileInp.readline().rstrip('\n')
    a, b, c = map(float, dongdautien.split())
    if a <= 0 and b <= 0 and c <= 0:
        thongBao = "cac canh cua tam giac phai lon hon khong !!!"
    elif a + b > c or a + c > b or b + c > a:
        if a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b:
            loaiTamGiac = "vuong"
            if a==b or a==c or b==c:
                loaiTamGiac = "vuong can"
        elif a==b and a==c: 
            loaiTamGiac = "deu"
        elif a==b or a==c or b==c:
            loaiTamGiac = "can"
        elif a*a > b*b + c*c or b*b > a*a + c*c or c*c > a*a + b*b:
            loaiTamGiac = "tu"
        else:
            loaiTamGiac = "nhon"
        thongBao = "{}, {}, {} la ba canh cua mot tam giac {}".format(a, b, c, loaiTamGiac)
    else:
        thongBao = "{}, {}, {} khong phai la ba canh cua mot tam giac {}".format(a, b, c, loaiTamGiac)

except FileNotFoundError:
    thongBao = "khong tim thay fileInp"
except: 
    thongBao = "Dinh Dang Dau Vao Khong Hop Le"
with open('bai10.1.output', 'w') as fileOut:
    fileOut.write(thongBao)
