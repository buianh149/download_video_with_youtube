try:
    a, b, c = map(int, input("Hay nhap cac so!").split())
    if(-1000 <= a <= 1000 and -1000 <= b <= 1000 and -1000 <= c <= 1000):
        print("tong cua {} + {} + {} = {}".format(a, b, c, a + b + c))
    else:
        print("khong nam trong pham vi")
except:
    print("dinh dang dau vao khong hop le!")