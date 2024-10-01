percobaan = 0
while percobaan < 3:
    print("Masukan username anda : ")
    usernameLogin = input()
    print("Masukan password anda : ")
    passwordLogin = input()

    if usernameLogin == "nazlasalsabila" and passwordLogin == "108":
        print("Selamat anda berhasil login!")
        ulang = "iya"
        while ulang == "iya":
            print("Masukkan harga mobil yang diinginkan :")
            hargaMobil = int(input())
            print("1. Tesla")
            print("2. Toyota")
            print("3. Hyundai")
            print("Pilih jenis mobil yang ingin dibeli : ")
            jenisMobil = input()

            if jenisMobil == "1":
                diskonTesla = hargaMobil * 0.17
                print("mobil Tesla seharga : ")
                print(diskonTesla)
                hSDtesla = hargaMobil - diskonTesla
                print("harga setelah diskon menjadi: ")
                print(hSDtesla)
                print("ulangi? (iya/tidak)")
                ulang = input()
                print("Keluar program? (iya/tidak)")
                keluarProgram = input()

                if keluarProgram == "iya":
                    percobaan = 3
                    ulang = "iyaa"
                    print("Anda berhasil keluar!")

                elif jenisMobil == "2":
                    diskonToyota = hargaMobil * 0.21
                    print("mobil Toyota seharga :")
                    print(diskonToyota)
                    hSDtoyota = hargaMobil - diskonToyota
                    print("harga setelah diskon menjadi :")
                    print(hSDtoyota)
                    print("ulangi? (iya/tidak)")
                    ulang = input()
                    print("Keluar program? (iya/tidak)")
                    keluarProgram = input()
                    if keluarProgram == "iya":
                        percobaan = 3
                        ulang = "iyaa"
                        print("Anda berhasil keluar!")
                
                elif jenisMobil == "3":
                    diskonHyundai = hargaMobil * 0.23
                    print("mobil Hyundai seharga :", end='', flush=True)
                    print(diskonHyundai)
                    hSDhyundai = hargaMobil - diskonHyundai
                    print("harga setelah diskon menjadi :")
                    print(hSDhyundai)
                    print("ulangi? (iya/tidak)")
                    ulang = input()
                    print("Keluar program? (iya/tidak)")
                    keluarProgram = input()
                    if keluarProgram == "iya":
                        percobaan = 3
                        ulang = "iyaa"
                        print("Anda berhasil keluar!")
                else:
                        print("Bu Navira tidak jadi membeli mobil")
    else:
        print("Mohon maaf login anda tidak berhasil!")
        percobaan = percobaan + 1
