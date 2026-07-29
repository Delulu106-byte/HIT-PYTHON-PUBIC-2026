danh_sach_san_pham = []

while True:
    try:
        n = int(input("Nhập số lượng sản phẩm: "))
        if n > 0:
            break
        print("Số lượng sản phẩm phải lớn hơn 0!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")


for i in range(n):
    print(f"\n--- Nhập sản phẩm thứ {i + 1} ---")
    
    while True:
        ma_sp = input("Nhập mã sản phẩm: ").strip()
        if not ma_sp:
            print("Mã sản phẩm không được để trống!")
            continue
        
        trung_ma = any(sp[0] == ma_sp for sp in danh_sach_san_pham)
        if trung_ma:
            print(f"Mã sản phẩm '{ma_sp}' đã tồn tại. Vui lòng nhập mã khác!")
        else:
            break

    ten_sp = input("Nhập tên sản phẩm: ").strip()

    while True:
        try:
            don_gia = float(input("Nhập đơn giá (> 0): "))
            if don_gia > 0:
                break
            print("Đơn giá phải lớn hơn 0!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")

    while True:
        try:
            so_luong = int(input("Nhập số lượng (>= 0): "))
            if so_luong >= 0:
                break
            print("Số lượng không được âm!")
        except ValueError:
            print("Vui lòng nhập một số nguyên hợp lệ!")

    san_pham = (ma_sp, ten_sp, don_gia, so_luong)
    danh_sach_san_pham.append(san_pham)

print("\n" + "=" * 60)
print("DANH SÁCH SẢN PHẨM VÀ THÀNH TIỀN")
print("=" * 60)
for sp in danh_sach_san_pham:
    ma_sp, ten_sp, don_gia, so_luong = sp
    thanh_tien = don_gia * so_luong
    print(f"Mã SP: {ma_sp} | Tên: {ten_sp} | Đơn giá: {don_gia:,.0f} | Số lượng: {so_luong} | Thành tiền: {thanh_tien:,.0f}")

sp_gia_tri_max = danh_sach_san_pham[0]
val_max = sp_gia_tri_max[2] * sp_gia_tri_max[3]

for sp in danh_sach_san_pham:
    val = sp[2] * sp[3]
    if val > val_max:
        val_max = val
        sp_gia_tri_max = sp

print("\n" + "-" * 60)
print(f"Sản phẩm có giá trị lớn nhất: {sp_gia_tri_max[1]} (Mã: {sp_gia_tri_max[0]}) với tổng giá trị: {val_max:,.0f}")


print("\n" + "-" * 60)
print("SẢN PHẨM SẮP HẾT HÀNG (Số lượng < 5):")
sp_sap_het = [sp for sp in danh_sach_san_pham if sp[3] < 5]
if sp_sap_het:
    for sp in sp_sap_het:
        print(f"- {sp[1]} (Mã: {sp[0]}) - Còn lại: {sp[3]}")
else:
    print("Không có sản phẩm nào sắp hết hàng.")
tong_gia_tri_kho = sum(sp[2] * sp[3] for sp in danh_sach_san_pham)
print("\n" + "-" * 60)
print(f"Tổng giá trị kho hàng: {tong_gia_tri_kho:,.0f}")


print("\n" + "=" * 60)
ma_tim_kiem = input("Nhập mã sản phẩm cần tìm kiếm: ").strip()
tim_thay = False

for sp in danh_sach_san_pham:
    if sp[0] == ma_tim_kiem:
        print(f" Tìm thấy thông tin sản phẩm:")
        print(f"  + Mã SP: {sp[0]}")
        print(f"  + Tên SP: {sp[1]}")
        print(f"  + Đơn giá: {sp[2]:,.0f}")
        print(f"  + Số lượng: {sp[3]}")
        print(f"  + Thành tiền: {sp[2] * sp[3]:,.0f}")
        tim_thay = True
        break

if not tim_thay:
    print(f"Không tìm thấy sản phẩm nào có mã '{ma_tim_kiem}'.")

