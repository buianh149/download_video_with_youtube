def soNguyenTo(n):
    if (n < 2):
        return False
    i = 2
    while i < n/2:
        if (n % i == 0):
            return False
            i +=1
        return True
a = [1,2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in a:
    print(i, end=" ")
    print("\n")
for i in a:
    if soNguyenTo(i):
        print(i, end" ")
