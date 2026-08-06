ds_hs = [
    { 
     "ten": "Nguyen Thi A",
     "diem":{
         "Toan":7,
         "Van":9,
         "Anh":10,
     }

    },
{ 
     "ten": "Tran Thi B",
     "diem":{
         "Toan":8,
         "Van":9,
         "Anh":7,
     }

    },
{ 
     "ten": "Pham Thi C",
     "diem":{
         "Toan":9,
         "Van":7,
         "Anh":5,
     }

    },    
]

sap_xe_Toan = sorted(
    ds_hs,
    key = lambda hs : hs ["diem"]["Toan"],
    reverse = True
)
print("Output 1: ")
for hs in sap_xe_Toan:
    print ( hs["ten"])

max_Anh = max(ds_hs, key = lambda hs : hs["diem"]["Anh"] )
print("Output 2: ")
print(max_Anh["ten"])

sap_xep_Tong = sorted(
    ds_hs,
    key = lambda hs: (
        -(hs["diem"]["Toan"] + hs["diem"]["Van"] + hs["diem"]["Anh"]),
        hs["ten"]
    )
)
print("Output 3: ")
for hs in sap_xep_Tong: 
    print(hs["ten"])

hs_gioi = filter(
    lambda hs : hs ["diem"]["Toan"] + hs["diem"]["Van"] + hs["diem"]["Anh"] >= 24,
    ds_hs
)
sap_xep_hsg = sorted(
    hs_gioi,
    key = lambda hs : hs ["diem"]["Toan"] + hs["diem"]["Van"] + hs["diem"]["Anh"],
    reverse=True
)
ten_hsg = list(map(lambda hs : hs["ten"], sap_xep_hsg))
print("Output 4: ")
print(ten_hsg)