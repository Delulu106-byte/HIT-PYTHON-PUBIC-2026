C = float(input("Nhap nhiet do do C :"))
while C > 100 or C < 0:
     C = float (input("Nhiet do khong hop le.Nhap lai do C :"))
doF = lambda C  :  C * 9 / 5 + 32
print (f"Nhiet do do F :{doF(C)}")

n = int(input("Nhap so nguyen n = "))
chan_le = lambda n :("Chan" if n % 2 == 0 else "Le")
print(f"{chan_le(n)}")

hoa_don = int(input("Nhap vao tong tien :"))
phan_tram_tip = int(input("% tip :"))
tien_tip = lambda hoa_don, phan_tram_tip: hoa_don * phan_tram_tip / 100
print(f"Tien tip : {tien_tip(hoa_don,phan_tram_tip)}")

ho_ten = input("Nhap ho va ten:")
tra_ve = lambda ho_ten : ho_ten.upper()
print(f"{tra_ve(ho_ten)}")