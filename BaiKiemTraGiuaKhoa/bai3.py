chuoi = input("nhap chuoi:")
target = input("nhap muc tieu:")
tu = chuoi.split()
vi_tri = []
for i in range(len(tu)):
    if tu[i] == target:
        vi_tri.append(str(i))
if len(vi_tri) == 0:
    print(-1)
else:
    print(" ".join(vi_tri))