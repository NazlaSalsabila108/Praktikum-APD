nama = ("Nazla Salsabila")
nim = ("2409106108")
harga_mobil_tesla = float(input("masukkan harga mobil tesla : Rp "))
harga_mobil_toyota = float(input("masukkan harga mobil toyota : Rp "))
harga_mobil_hyundai = float(input("masukkan harga mobil hyundai : Rp "))

diskon_tesla = 0.17
diskon_toyota = 0.21
diskon_hyundai = 0.23

diskon_mobil1 = harga_mobil_tesla * diskon_tesla
diskon_mobil2 = harga_mobil_toyota * diskon_hyundai
diskon_mobil3 = harga_mobil_hyundai * diskon_hyundai

harga_setelah_diskon1 = harga_mobil_tesla - diskon_mobil1
harga_setelah_diskon2 = harga_mobil_toyota - diskon_mobil2
harga_setelah_diskon3 = harga_mobil_hyundai- diskon_mobil3 

modulus_tesla = int(harga_mobil_tesla)/7
modulus_toyota = int(harga_mobil_toyota)/7
modulus_hyundai = int(harga_mobil_hyundai)/7

print(f"{nama}, dengan nim {nim} ingin membeli mobil tesla seharga : { harga_mobil_tesla}")
print(f"{nama}, dengan nim {nim} ingin membeli mobil toyota harga : { harga_mobil_toyota}")
print(f"{nama}, dengan nim {nim} ingin membeli mobil hyundai seharga : { harga_mobil_hyundai}")
print(f"mobil tesla seharga {harga_mobil_tesla} diskon 17% menjadi {diskon_mobil1}")
print(f"mobil toyota seharga {harga_mobil_toyota} diskon 21% menjadi {diskon_mobil2}")
print(f"mobil hyundai seharga {harga_mobil_hyundai} diskon 23% menjadi {diskon_mobil3}")
print("harga setiap mobil tesla modulus 7 adalah", modulus_tesla)
print("harga setiap mobil toyota modulus 7 adalah", modulus_toyota)
print("harga setiap mobil hyundai modulus 7 adalah", modulus_hyundai)