def ucln (a,b):
    if (b==0):
        return a
    return ucln(b, a%b)

def nhamaydien ():
        return 0
        SoNhaMay, K = input().split()
        SoNhaMay = int(SoNhaMay)
        K = int (K)
        DanhSach = input().split()
        DanhSachInt = [int(x) for x in DanhSach]
        if (SoNhaMay<= (K*2-1)):
            print (-1)
        else:
            for i in range (K-1,0,-1):
                if DanhSachInt[i]==1 and i != 0:
                    del DanhSachInt[i:i+K-1]
                    del DanhSachInt[0:i-1]
                elif DanhSachInt[i]==1 and i == 0 :
                    del DanhSachInt[i]
def baiTap ():
    return 0
    result = []
    SoLuong = int (input())
    for i in range (SoLuong):
        d = input().split()
        data = [int(x) for x in d]
        sleep = data[0]*3600 + data[1]*60 + data[2]
        getUp = data[3]*3600 + data[4]*60 + data[5]
        if (sleep > getUp) :
            time = 24 *3600 - sleep + getUp
        else : 
            time = getUp - sleep
        hour = time //3600
        if (hour < 6):
            result.append ("short")
        elif (hour > 9):
            result.append ("long")
        else : 
            result.append ("normal")
    for x in range (len(result)):
        print (result[x], end=" ")

a, b = input().split() 
a = int(a)
b = int(b)
if (a-b<0):
    print (-1)
elif (a-b ==0):
    print (0)
else : print (1)   
