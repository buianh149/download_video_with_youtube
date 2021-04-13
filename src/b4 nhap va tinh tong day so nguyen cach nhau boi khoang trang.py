"""
 map(function, iterable, ...)
 trong do:  function: Hàm thực thi cho từng phần tử trong iterable.
            iterable: một list, tuple, dictionary... muốn duyệt.
"""

dayGiaTri = input("Nhap day so can tinh: ")
danhSachGiaTri = dayGiaTri.split()
try:
    danhSachSo = map(int, danhSachGiaTri)
    tongDaySo = sum(danhSachSo)
    print("tong day so la: ", tongDaySo)
except:
    print("Dinh dang khong dung, vui long nhap lai!")

""" 
#  cac ham binh thuong thuong dinh nghia bang tu khoa "def"
# vd1:
def binhPhuong(n):
    return n*n
number = (2, 4, 5)
result = map(binhPhuong, number)
print(list(result))
"""
"""
# cac ham vo danh thi dinh nghia la "lambda"
#  vd2: truyen 1 iterable
number = (2, 4, 6)
result = map(lambda n: n * n, number)
print(list(result))
""" 
"""
# vd3: truyen nhieu iterable
num1 = [2, 4 ,6, 7]
num2 = [1, 5, 3, 2]
num3 = [3, 4 ,5 ,2]
result = map(lambda n1, n2, n3: n1 + n2 + n3, num1, num2, num3)
print(list(result))
"""