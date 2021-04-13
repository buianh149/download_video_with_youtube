with open('bai1.10.inp', 'r') as fileInp:
    ten = fileInp.readline().rstrip('\n')
    tuoiHienTai = int(fileInp.readline())
with open('bai1.10.out', 'w') as fileout:
    fileout.write = ('vao hai muoi nam nua, tuoi cua {} se la {}'.format(ten, tuoiHienTai + 20))