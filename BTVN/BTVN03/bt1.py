# Nhap chuoi
s = input("Nhap chuoi : ")
# Dao nguoc 
dao_nguoc = ""
for i in range(len(s) - 1, -1, -1):
    dao_nguoc += s[i]
print("Chuoi dao nguoc : ", dao_nguoc)
# Sapxep 
ds = list(s)
ds.sort()
chuoi_sap_xep = ""
for ky_tu in ds:
    chuoi_sap_xep += ky_tu
print("Chuoi sau khi sap xep la : ", chuoi_sap_xep)
# Ktra chuoi doi xung 
if s == dao_nguoc:
    print("Day la chuoi doi xung!")
else:
    print("Day khong phai la chuoi doi xung!")
# Tim ky tu xuat hien nhieu nhat
tap_ky_tu = set(s)
max_dem = 0
for ky_tu in tap_ky_tu:
    if s.count(ky_tu) > max_dem:
        max_dem = s.count(ky_tu)
ket_qua = []
for ky_tu in tap_ky_tu:
    if s.count(ky_tu) == max_dem:
        ket_qua.append(ky_tu)
ket_qua.sort()
print("Ky tu xuat hien nhieu nhat :")
for ky_tu in ket_qua:
    print(ky_tu, end=" ")
print()
print("So lan xuat hien", max_dem)
# Ktra du 5 nguyen am : 
chuoi_thuong = s.lower()
if "a" in chuoi_thuong and "e" in chuoi_thuong and "i" in chuoi_thuong and "o" in chuoi_thuong and "u" in chuoi_thuong:
    print("Chuoi chua day du 5 nguyen am Tieng Anh!")
else:
    print("Chuoi khong chua day du 5 nguyen am Tieng Anh!")
