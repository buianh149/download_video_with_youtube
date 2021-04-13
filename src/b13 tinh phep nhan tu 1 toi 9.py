try:
    n = int(input("Nhập số cần tính: "))
    if n < 1 or n > 9:
        print("chỉ tính phép nhân số từ 1 tới 9 !!!")
    else:
        for i in range(1, 10):
            print("{} x {} = {}".format(n, i, n * i))
except:
    print("Dinh danh dau vao khong dung!")