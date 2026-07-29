# Nhap so luong khoan chi
n = int(input("Nhap so luong khoan chi: "))
ds = []
# Nhap cac khoan chi
for i in range(n):
    du_lieu = input().split(",")
    ten = du_lieu[0].strip().title()
    so_tien = int(du_lieu[1].strip())
    danh_muc = du_lieu[2].strip().title()
    khoan_chi = (ten, so_tien, danh_muc)
    ds.append(khoan_chi)
# In danh sach
print("Danh sach cac khoan chi:")
for khoan_chi in ds:
    print(khoan_chi)
# Tong chi tieu
tong = 0
for khoan_chi in ds:
    tong += khoan_chi[1]
print("Tong chi tieu:", tong, "VND")
# Thong ke theo danh muc
print("Thong ke theo danh muc:")
tap_danh_muc = set()
for khoan_chi in ds:
    tap_danh_muc.add(khoan_chi[2])
for danh_muc in tap_danh_muc:
    so_khoan = 0
    tong_tien = 0
    for khoan_chi in ds:
        if khoan_chi[2] == danh_muc:
            so_khoan += 1
            tong_tien += khoan_chi[1]
    print(danh_muc + ":")
    print("- So khoan chi:", so_khoan)
    print("- Tong tien:", tong_tien, "VND")
# Kiem tra vuot muc chi tieu
if tong > 5000000:
    print("Tong chi tieu vuot qua 5000000 VND.")
# Tim khoan chi lon nhat
lon_nhat = ds[0]
for khoan_chi in ds:
    if khoan_chi[1] > lon_nhat[1]:
        lon_nhat = khoan_chi
print("Khoan chi co so tien lon nhat:")
print(lon_nhat)