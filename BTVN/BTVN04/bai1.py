def quan_ly_kho(kho_hang, sp_moi,sp_xoa):
    so_luong_laptop = kho_hang.get("Laptop",0)
    print("So luong laptop:",so_luong_laptop)

    kho_hang.update(sp_moi)

    kq_xoa = kho_hang.pop(sp_xoa,"Khong ton tai")
    print(f"San pham xoa : {sp_xoa}" ,kq_xoa)

    print("Kho hang :",kho_hang.items())

    tong = sum(kho_hang.values())
    print("Tong sp trong kho :", tong)

kho_hang = {"Laptop":20,"Chuot":20,"Man hinh":20}
sp_moi = {"Ban phim":20, "Chuot": 10}
sp_xoa = "Man hinh"

quan_ly_kho(kho_hang,sp_moi,sp_xoa)