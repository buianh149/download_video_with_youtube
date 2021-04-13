#Khoi lenh co the phat sinh loi
try:
   #Nhap hai so tu ban phim
   #Ep kieu du lieu sang so nguyen
   a = int(input())
   b = int(input())
  
   if a>b:
       print("So thu nhat lon hon so thu hai!")
   else:       
       dem = 0
       #Su dung vong lap for duyet cac gia tri tu a den b
       for i in range(a, b+1):
           #Kiem tra dieu kien chia het cho 5
           if i % 5 == 0:
               #Dem cac so thoa dieu kien
               dem += 1
               #Kiem tra vuot qua 10 so hay chua
               if dem > 10:
                   print("\nIn qua 10 so roi!")
                   #Thoat vong lap
                   break
               print(i, end=" ")
       #Neu khong gap lenh break thi se thuc hien lenh else
       else:
           if dem == 0:
               print("Khong co so nao chia het cho 5")
           else:
               print("\nDa in het cac so chia het cho 5")
              
#Khoi lenh duoc thuc thi khi loi xay ra
except:
   print("Dinh dang dau vao khong hop le!")
