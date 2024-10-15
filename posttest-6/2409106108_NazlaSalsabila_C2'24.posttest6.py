list_akun = [
    {
        "nama": "nazlasalsabila",
        "password": "108"
    }
]

print("Hallo! Selamat datang di aplikasi manajemen informasi kesehatan")
print("Pada aplikasi ini pasien diminta untuk memberikan keterangan riwayat penyakit sebelumnya dan memasukkan resep obat")

while True:
    print("Silahkan pilih 'Daftar akun' jika anda belum membuat akun, dan jika sudah memiliki akun silahkan pencet 'Login'")
    print("1. Daftar akun!")
    print("2. Silahkan Login!")
    print("3. Exit")
    print("_________________________________")

    opsi = input("Silahkan pilih opsi di atas: ")
    print(" ")

    if opsi == "1":
        print("Hallo pengguna baru! Ayo buat akun anda terlebih dahulu ya")
        username = input("Username: ")

        for akun in list_akun:
            if akun["nama"] == username:
                print("Nama ini sudah terpakai untuk registrasi mohon maaf, silahkan dicoba lagi\n")
                break
        else:
            password = input("Password: ")
            list_akun.append({"nama": username, "password": password})
            print(f"Akun anda berhasil terdaftar dengan ID: {username}\n")

    elif opsi == "2":
        print("Hallo! Silahkan Login terlebih dahulu ya!")
        username = input("Username: ")
        password = input("Password: ")

        for akun in list_akun:
            if akun["nama"] == username and akun["password"] == password:
                print(f"\n Selamat datang {username}!")
                list_obat = {
                    "Riwayat Penyakit": ["Maag", "Asma", "Diare", "Ambeien" ],
                    "Resep Obat": ["Promaag", "Astharol", "Entrostop", "Ambeven"]
                }

                while True:
                    print("--------Silahkan pilih yang ingin anda lakukan!--------")
                    print("1. Tambahkan riwayat penyakit dan resep obat")
                    print("2. Lihat riwayat penyakit dan resep obat yang ada")
                    print("3. Edit obat dan resep yang ada")
                    print("4. Hapus obat dan resep yang ada")
                    print("5. Exit")
                    print("____________________________________________")

                    opsi = input("Pilih opsi: ")
                    print(" ")

                    if opsi == "1":
                        riwayat_penyakit = input("Riwayat penyakit: ")
                        resep_obat = input("Resep obat: ")
                        list_obat["Riwayat Penyakit"].append(riwayat_penyakit)
                        list_obat["Resep Obat"].append(resep_obat)

                        print("Riwayat penyakit dan resep obat anda sudah disimpan!\n")

                    elif opsi == "2":
                        if not list_obat["Riwayat Penyakit"] and not list_obat["Resep Obat"]:
                            print("Opps, saat ini pasien belum punya resep obat, silahkan beritahu riwayat penyakit terlebih dahulu.\n")
                        else:
                            for i in range(len(list_obat["Riwayat Penyakit"])):
                                print(f"{i + 1}. Riwayat Penyakit: {list_obat['Riwayat Penyakit'][i]}, Resep Obat: {list_obat['Resep Obat'][i]}")
                            print(" ")

                    elif opsi == "3":
                        if not list_obat["Riwayat Penyakit"]:
                            print("Tidak ada resep obat yang bisa diedit.")
                        else:
                            for i in range(len(list_obat["Riwayat Penyakit"])):
                                print(f"{i + 1}. Riwayat Penyakit: {list_obat['Riwayat Penyakit'][i]}, Resep Obat: {list_obat['Resep Obat'][i]}")
                            print(" ")
                            update_data = int(input("Resep obat nomor berapa yang ingin anda edit: ")) - 1

                            if update_data < 0 or update_data >= len(list_obat["Riwayat Penyakit"]):
                                print("Tidak ada resep obat yang anda maksud, mohon maaf silahkan input ulang!\n")
                            else:
                                riwayat_penyakit_baru = input("Masukkan riwayat penyakit terbaru: ")
                                resep_obat_baru = input("Masukkan obat dan resep terbaru: ")
                                print("Apa anda yakin ingin mengedit resep obat?")
                                print("1. Iya")
                                print("2. Tidak")
                                konfirmasi = input("Pilih opsi: ")

                                if konfirmasi == "1":
                                    print("Resep obat yang anda pilih sudah di edit ya!\n")
                                    print(f"Sebelum: Riwayat Penyakit: {list_obat['Riwayat Penyakit'][update_data]}, Resep Obat: {list_obat['Resep Obat'][update_data]}\n")

                                    list_obat["Riwayat Penyakit"][update_data] = riwayat_penyakit_baru
                                    list_obat["Resep Obat"][update_data] = resep_obat_baru

                                    print(f"Sesudah: Riwayat Penyakit: {list_obat['Riwayat Penyakit'][update_data]}, Resep Obat: {list_obat['Resep Obat'][update_data]}\n")

                                elif konfirmasi == "2":
                                    print("Tindakan untuk mengedit resep obat anda dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")

                    elif opsi == "4":
                        if not list_obat["Riwayat Penyakit"]:
                            print("Tidak ada resep obat yang bisa dihapus.")
                        else:
                            for i in range(len(list_obat["Riwayat Penyakit"])):
                                print(f"{i + 1}. Riwayat Penyakit: {list_obat['Riwayat Penyakit'][i]}, Resep Obat: {list_obat['Resep Obat'][i]}")
                            print(" ")

                            hapus_data = int(input("Resep obat apakah yang ingin dihapus: ")) - 1

                            if hapus_data < 0 or hapus_data >= len(list_obat["Riwayat Penyakit"]):
                                print("Tidak ada resep obat yang anda maksud, mohon maaf silahkan input ulang\n")
                            else:
                                print(f"Apa anda yakin ingin menghapus resep obat ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                konfirmasi = input("Pilih: ")
                                if konfirmasi == "1":
                                    del list_obat["Riwayat Penyakit"][hapus_data]
                                    del list_obat["Resep Obat"][hapus_data]
                                    print("Resep obat yang anda pilih sudah dihapus!\n")
                                elif konfirmasi == "2":
                                    print("Tindakan untuk menghapus dibatalkan")
                                else:
                                    print("Mohon pilih '1' atau '2'")

                    elif opsi == "5":
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
