while True:
    try:
        n = int(input("Nhập số lượng sinh viên: "))
        if n > 0:
            break
        print("Số lượng sinh viên phải lớn hơn 0. Vui lòng nhập lại!")
    except ValueError:
        print("Vui lòng nhập một số nguyên hợp lệ!")

diem_list = []


for i in range(n):
    while True:
        try:
            diem = float(input(f"Nhập điểm sinh viên thứ {i + 1} (0 - 10): "))
            if 0 <= diem <= 10:
                diem_list.append(diem)
                break
            else:
                print("Điểm phải nằm trong khoảng từ 0 đến 10. Vui lòng nhập lại!")
        except ValueError:
            print("Vui lòng nhập một số hợp lệ!")


tong_diem = sum(diem_list)
diem_trung_binh = tong_diem / n


diem_max = diem_list[0]
diem_min = diem_list[0]

for diem in diem_list:
    if diem > diem_max:
        diem_max = diem
    if diem < diem_min:
        diem_min = diem


diem_tren_tb = [diem for diem in diem_list if diem > diem_trung_binh]


co_diem_10 = 10 in diem_list


print("\n" + "=" * 30)
print("KẾT QUẢ QUẢN LÝ ĐIỂM")
print("=" * 30)
print(f"Danh sách điểm: {diem_list}")
print(f"Điểm trung bình: {diem_trung_binh:.2f}")
print(f"Điểm lớn nhất: {diem_max}")
print(f"Điểm nhỏ nhất: {diem_min}")
print(f"Các điểm lớn hơn điểm trung bình: {diem_tren_tb}")

if co_diem_10:
    print("Có sinh viên đạt điểm 10.")
else:
    print("Không có sinh viên nào đạt điểm 10.")