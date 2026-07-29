# Nhap
input1 = input("Nhap so thich cua nguoi A: ")
input2 = input("Nhap so thich cua nguoi B: ")
# list va chuan hoa
ds_a = input1.split(",")
ds_b = input2.split(",")
for i in range(len(ds_a)):
    ds_a[i] = ds_a[i].strip().title()
for i in range(len(ds_b)):
    ds_b[i] = ds_b[i].strip().title()
# Chuyen set
set_a = set(ds_a)
set_b = set(ds_b)
print("Cac so thich cua nguoi A:")
print(set_a)
print("Cac so thich cua nguoi B:")
print(set_b)
# So thich chung
so_thich_chung = set_a & set_b
print("So thich chung:")
if len(so_thich_chung) == 0:
    print("Khong co so thich chung.")
else:
    print(so_thich_chung)
# So thich chi nguoi A co
print("So thich chi nguoi A co:")
print(set_a - set_b)
# Tat ca so thich
print("Tat ca so thich:")
print(set_a | set_b)
# Do tuong dong
tong_so_thich = set_a | set_b
if len(tong_so_thich) == 0:
    do_tuong_dong = 0
else:
    do_tuong_dong = len(so_thich_chung) / len(tong_so_thich) * 100
print("Do tuong dong: %.2f%%" % do_tuong_dong)