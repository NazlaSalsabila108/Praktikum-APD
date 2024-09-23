harga_mobil = 450000000
jenis_mobil = input("Masukkan jenis mobil : ")

diskon_tesla = 0.17
diskon_toyota = 0.21
diskon_hyundai = 0.23

diskon_mobil1 = harga_mobil * diskon_tesla
diskon_mobil2 = harga_mobil * diskon_hyundai
diskon_mobil3 = harga_mobil * diskon_hyundai

harga_setelah_diskon1 = harga_mobil - diskon_mobil1
harga_setelah_diskon2 = harga_mobil - diskon_mobil2
harga_setelah_diskon3 = harga_mobil - diskon_mobil3 

if   jenis_mobil == "tesla" : 
    diskon_mobil = harga_mobil * diskon_tesla 
    harga_setelah_diskon1 = harga_mobil - diskon_mobil1
    print(f"Mobil tesla seharga {diskon_mobil1} diskon 17% menjadi {harga_setelah_diskon1} ")
elif jenis_mobil == "toyota" :
    diskon_mobil2 = harga_mobil * diskon_toyota 
    harga_setelah_diskon2 = harga_mobil - diskon_mobil2
    print(f"Mobil toyota seharga {diskon_mobil2} diskon 21% menjadi {harga_setelah_diskon2} ")
elif jenis_mobil == "hyundai" :
    diskon_mobil3 = harga_mobil * diskon_hyundai
    harga_setelah_diskon3 = harga_mobil * diskon_mobil3
    print(f"Mobil hyundai seharga {diskon_mobil3} diskon 23% menjadi {harga_setelah_diskon3}" )
else :
    print("Ibu Navira tidak jadi membeli mobil")