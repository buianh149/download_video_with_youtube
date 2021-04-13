try:
    a, b, c = map(float, input().split())
    print("canh thu nhat: ", a)
    print("canh thu hai: ", b)
    print("canh thu ba: ", c)
    if a <= 0 or b <= 0 or c <=0:
        print("canh tam giac khong duoc nho hon hoac bang khong")
    elif a + b > c and a + c > b and b + c > a:
        print("tao dc tam giac!")
    else:
        print("khong tao duoc tam giac!")
except:
    print("dinh dang khong dung!")