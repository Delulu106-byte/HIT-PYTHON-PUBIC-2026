gia = int(input("nhap gia:"))
tra = int(input("so tien khach dua:"))
thua = tra - gia
menh_gia = [20, 10, 5, 2, 1]
tong = 0
for x in menh_gia:
    tong += thua // x
    thua %= x
print(tong)