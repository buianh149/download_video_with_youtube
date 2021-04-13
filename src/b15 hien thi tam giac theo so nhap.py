try:
    n = int(input(" hay nhap so: "))
    if n < 1 or n > 20:
        print("nhap so tu 1 toi 20 !")
    else:
        for hang in range(n):
            for cot in range(n - hang, 0 ,-1):
                print(cot, end=" ")
            print()
except:
    print("dinh dang dau vao khong dung")