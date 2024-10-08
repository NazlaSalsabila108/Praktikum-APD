list_akun = []

print("Hallo! Selamat datang di aplikasi manajemen informasi kesehatan")
print("Pada aplikasi ini pasien diminta untuk memberikan keterangan riwayat penyakit sebelumnya dan memasukkan resep obat")

while True:
    print("Silahkan pilih 'Daftar akun' jika anda belum membuat akun, dan jika sudah memiliki akun silahkan pencet 'Login'")
    print("1. Daftar akun!")
    print("2. Silahkan Login!")
    print("3. Exit")
    print("_________________________________")

    opsi = input("Silahkan pilih opsi di atas : ")
    print(" ")

    if opsi == "1":
        print("Hallo pengguna baru! Ayo buat akun anda terlebih dahulu ya")
        username = input("Username : ")

        for akun in list_akun:
            if akun[0] == username:
                print("Nama ini sudah terpakai untuk registrasi mohon maaf, silahkan dicoba lagi\n")
                break
        else:
            password = input("Password: ")
            list_akun.append([username, password])
            print(f"Akun anda berhasil terdaftar dengan ID : {username}\n")
    
    elif opsi == "2":

        print("Hallo! Silahkan Login terlebih dahulu ya!")
        username = input("Username : ")
        password = input("Password : ")

        for akun in list_akun:
            if username != akun[0] or password != akun[1]:
                print("Username atau password anda salah, silahkan dicoba lagi\n")

            else:
                print(f"\nSelamat datang {username}!")
                list_obat = []

                while True:
                    print("--------Silahkan pilih yang ingin anda lakukan!--------")
                    print("1. Tambahkan riwayat penyakit dan resep obat")
                    print("2. Lihat riwayat penyakit dan resep obat yang ada")
                    print("3. Edit obat dan resep yang ada")
                    print("4. Hapus obat dan resep yang ada ")
                    print("5. Exit")
                    print("____________________________________________")

                    option = input("Pilih opsi : ")
                    print(" ")

                    if option == "1":
                        riwayat_penyakit = input("Riwayat penyakit : ")
                        resep_obat = input("Resep obat : ")
                        list_obat.append([riwayat_penyakit, resep_obat])

                        print("Resep obat anda sudah disimpan!\n")

                    elif option == "2":
                        if list_obat == []:
                            print("Opps, saat ini pasien belum punya resep obat, silahkan beritahu riwayat penyakit terlebih dahulu.\n")
                        else:
                            for data in list_obat:
                                print(f"{list_obat.index(data) + 1}. Riwayat Penyakit : {data[0]}, Resep Obat : {data[1]}")
                            print(" ")

                    elif option == "3":
                        if list_obat == []:

                            print("Tidak ada resep obat yang bisa diedit.")
                        else:
                            for data in list_obat:
                                print(f"{list_obat.index(data) + 1}. Riwayat Penyakit : {data[0]}, Resep Obat : {data[1]}")

                            print(" ")
                            update_data = int(input("Resep obat nomor berapa yang ingin anda edit : ")) - 1

                            if update_data < 0 or update_data >= len(list_obat):
                                print("Tidak ada resep obat yang anda maksud, mohon maaf silahkan input ulang!\n")
                            else:
                                riwayat_penyakit_baru = input("Masukkan riwayat penyakit terbaru: ")
                                resep_obat_baru = input("Masukkan obat dan resep terbaru : ")
                                print("Apa anda yakin ingin mengedit resep obat ?")
                                print("1. Iya")
                                print("2. Tidak")
                                confirmation = input("Pilih opsi : ")

                                if confirmation == "1":
                                    print("Resep obat yang anda pilih sudah di edit ya!\n")
                                    print(f"Sebelum :")
                                    print(f"Riwayat Penyakit : {list_obat[update_data][0]}, Resep Obat : {list_obat[update_data][1]}\n")

                                    list_obat[update_data][0] = riwayat_penyakit_baru
                                    list_obat[update_data][1] = resep_obat_baru

                                    print(f"Sesudah :")
                                    print(f"Riwayat Penyakit : {list_obat[update_data][0]}, Resep Obat : {list_obat[update_data][1]}\n")

                                elif confirmation == "2":
                                    print("Tindakan untuk mengedit resep obat anda dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                    
                    elif option == "4":
                        if list_obat == []:
                            print("Tidak ada resep obat yang bisa dihapus.")
                        else:
                            for data in list_obat:
                                print(f"{list_obat.index(data) + 1}. Riwayat Penyakit : {data[0]}, Resep Obat : {data[1]}")
                            print(" ")

                            delete_data = int(input("Resep obat apakah yang ingin dihapus: ")) - 1

                            if delete_data< 0 or delete_data >= len(list_obat):
                                print("Tidak ada resep obat yang anda maksud, mohon maaf silahkan input ulang\n")
                            else:
                                print(f"Apa anda yakin ingin menghapus resep obat ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                confirmation = input("Pilih: ")
                                if confirmation == "1":
                                    del list_obat[delete_data]  # Menghapus resep obat dari list
                                    print("Resep obat yang anda pilih sudah dihapus!\n")
                                elif confirmation == "2":
                                    print("Tindakan untuk menghapus dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")
                            

                    elif option == "5":
                        print("Aplikasi Manajemen Informasi Kesehatan ditutup.\n")
                        break
                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")
                break

    elif opsi == "3":
        print("Apakah anda yakin ingin keluar dari aplikasi ini? ")
        print("1. Iya")
        print("2. Tidak")
        pilih = input("Input pilihan: ")
        print(" ")
        if pilih == "1":
            print("Terimakasih sudah menggunakan aplikasi ini, semoga cepat sembuh dan segera pulih ya!")
            break
        elif pilih == "2":
            continue
        else:
            print("Input tidak valid, silahkan pilih '1' atau '2'\n")
    else:
        print("Input tidak valid, silahkan pilih 1, 2, atau 3")
