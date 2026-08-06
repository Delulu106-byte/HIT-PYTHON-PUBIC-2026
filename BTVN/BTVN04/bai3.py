ds_sp = [
    {
        "ma_sp": "SP01",
        "ten_sp": "Laptop Asus",
        "loai": "Dien tu",
        "gia": 18000000,
        "so_luong": 8
    },
    {
        "ma_sp": "SP02",
        "ten_sp": "Chuot Logitech",
        "loai": "Phu kien",
        "gia": 450000,
        "so_luong": 25
    },
    {
        "ma_sp": "SP03",
        "ten_sp": "Dien thoai Samsung",
        "loai": "Dien tu",
        "gia": 12000000,
        "so_luong": 0
    },
    {
        "ma_sp": "SP04",
        "ten_sp": "Ban phim co",
        "loai": "Phu kien",
        "gia": 1500000,
        "so_luong": 10
    },
    {
        "ma_sp": "SP05",
        "ten_sp": "May in Canon",
        "loai": "Dien tu",
        "gia": 3200000,
        "so_luong": 5
    }
]

thuoc_dien_tu = list(filter(lambda sp : sp["loai"],ds_sp))
print("SP thuoc danh muc Dien tu:")
for sp in thuoc_dien_tu:
    print (sp["ten_sp"])

ton_kho =list(filter(lambda sp : sp["so_luong"] > 0 ,ds_sp))
print("San pham ton kho:")
for ds in ton_kho :
    print(sp["ten_sp"])

ten_sp = list(map(lambda sp : sp["ten_sp"],ds_sp))
print ("Danh sach ten sp:")
print (ten_sp)

vip = filter(
    lambda sp : sp["gia"] >= 1000000,ds_sp
)
discount = list(map(lambda sp : f" Tang voucher 100k khi mua sp {sp["ten_sp"]}",vip))