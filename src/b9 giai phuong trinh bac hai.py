import math
try: 
    a, b, c = map(float, input().split())
    print("he so bac hai:", a)
    print("he so bac nhat:", b)
    print("he so tu do:", c)
    if a == 0:
        if b == 0:
            if c == 0:
                print("phuong trinh co vo so nghiem !")
            else:
                print("phuong trinh vo nghiem !")
        else:
            print("phuong trinh co mot nghiem ", (-c / b))
    else:
        denTa =(b * b - 4 * a * c)
        if denTa == 0:
            print("phuong trinh co nghiem kep x1 = x2 = ", (-b /(2 * a)))
        elif denTa < 0:
            print("phuong trinh vo nghiem !")
        else:
            x1 = float((-b + math.sqrt(denTa))/(2 * a))
            x2 = float((-b - math.sqrt(denTa))/(2 * a))
            print("phuong trinh co hai nghiem x1 = {}, x2 = {}".format(x1, x2))
except:
    print("Dinh Dang Khong Dung!")           