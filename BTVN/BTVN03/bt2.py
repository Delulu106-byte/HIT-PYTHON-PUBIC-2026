# Nhap du lieu
input1 = input("Nhap cac san pham: ")
input2 = input("Nhap san pham can kiem tra: ")
# Tao list va chuan hoa
ds = input1.split(",")
for i in range(len(ds)):
    ds[i] = ds[i].strip().title()
print("Danh sach san pham:")
print(ds)
# Tong so san pham
print("Tong so san pham da mua:", len(ds))
# San pham o vi tri giua
if len(ds) % 2 != 0:
    print("San pham o vi tri giua:", ds[len(ds) // 2])
# san pham mua nhieu nhat
tap_san_pham = set(ds)
max_dem = 0
for san_pham in tap_san_pham:
    if ds.count(san_pham) > max_dem:
        max_dem = ds.count(san_pham)
ket_qua = []
for san_pham in tap_san_pham:
    if ds.count(san_pham) == max_dem:
        ket_qua.append(san_pham)
ket_qua.sort()
print("Cac san pham duoc mua nhieu nhat:")
for san_pham in ket_qua:
    print(san_pham + ":", max_dem, "lan")
# Kiem tra san pham 
input2 = input2.strip().title()
if input2 in ds:
    print(input2, "da duoc mua", ds.count(input2), "lan.")
else:
    print(input2, "chua duoc mua.")
# update danh sach
ds.insert(0, "Banh Nabati")
if "Sua" in ds:
    ds.remove("Sua")
print("Danh sach sau khi cap nhat:")
print(ds)