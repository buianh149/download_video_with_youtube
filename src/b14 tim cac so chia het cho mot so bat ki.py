try:
    
    a, b = map(int, input(" xin moi nhap so, hay cach ra khi xong mot so ").split())
    print("So can tim boi so la: {}".format(5))
    print("Khoang can tim la {} => {}".format(a, b))
   
    if a > b:
        print("so thu nhat khong duoc lon hon so thu hai !")
    else: 
        dem = o
        for i in range(a, b + 1):
            if i % 5 == 0:
                dem += 1
                if dem > 10:
                    print("Da qua 10 so !")
                    break
                print(i, end=" ")
            else:
                if dem == 0:
                    print("khong co so nao chia het cho {}".format(5))
                else:
                    print("\nDa in het so chia het cho {}".format(5))
except:
    print("Dinh dang dau vao khong dung!")
