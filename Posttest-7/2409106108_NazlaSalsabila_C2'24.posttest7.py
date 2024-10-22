list_akun = [
    {
        "nama": "nazlasalsabila",
        "password": "108"
    }
]
list_obat = {
    "Riwayat Penyakit": ["Maag", "Asma", "Diare", "Ambeien"],
    "Resep Obat": ["Promaag", "Astharol", "Entrostop", "Ambeven"]
}
pengguna_saat_ini = None 

# Fungsi 1 :
def cek_akun(username):
    """Fungsi ini mengecek apakah username sudah terdaftar."""
    for akun in list_akun:
        if akun["nama"] == username:
            return True
    return False

# Fungsi 2 : (dengan parameter)
def tambah_obat(riwayat_penyakit, resep_obat):
    """Menambahkan riwayat penyakit dan resep obat baru ke dalam list_obat."""
    list_obat["Riwayat Penyakit"].append(riwayat_penyakit)
    list_obat["Resep Obat"].append(resep_obat)
    print("Riwayat penyakit dan resep obat berhasil ditambahkan.\n")

# Fungsi 3 : (tanpa parameter)
def tampilkan_obat():
    """Menampilkan seluruh riwayat penyakit dan resep obat yang ada."""
    if not list_obat["Riwayat Penyakit"] and not list_obat["Resep Obat"]:
        print("Tidak ada riwayat penyakit dan resep obat yang tersimpan.\n")
    else:
        for i in range(len(list_obat["Riwayat Penyakit"])):
            print(f"{i + 1}. Riwayat Penyakit: {list_obat['Riwayat Penyakit'][i]}, Resep Obat: {list_obat['Resep Obat'][i]}")
        print(" ")

# Prosedur 1 :
def prosedur_daftar():
    """Prosedur untuk mendaftarkan pengguna baru."""
    username = input("Username: ")

    if cek_akun(username):
        print("Username sudah terpakai, silahkan gunakan username lain.\n")
    else:
        password = input("Password: ")
        list_akun.append({"nama": username, "password": password})
        print(f"Akun berhasil terdaftar dengan ID: {username}\n")

# Prosedur 2 : 
def prosedur_login():
    """Prosedur untuk login pengguna."""
    global pengguna_saat_ini  
    username = input("Username: ")
    password = input("Password: ")

    if cek_akun(username):
        for akun in list_akun:
            if akun["nama"] == username and akun["password"] == password:
                pengguna_saat_ini = username  
                print(f"\nSelamat datang {username}!\n")
                return True
        print("Password salah. Silahkan coba lagi.\n")
    else:
        print("Akun tidak ditemukan. Silahkan daftar terlebih dahulu.\n")
    return False


def main():
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
            prosedur_daftar()
        elif opsi == "2":
            if prosedur_login():
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
                        tambah_obat(riwayat_penyakit, resep_obat)

                    elif opsi == "2":
                        tampilkan_obat()

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
                                    list_obat["Riwayat Penyakit"][update_data] = riwayat_penyakit_baru
                                    list_obat["Resep Obat"][update_data] = resep_obat_baru
                                    print("Resep obat berhasil diedit!\n")
                                elif konfirmasi == "2":
                                    print("Edit dibatalkan.")
                                else:
                                    print("Mohon pilih '1' atau '2'")

                    elif opsi == "4":
                        if not list_obat["Riwayat Penyakit"]:
                            print("Tidak ada resep obat yang bisa dihapus.")
                        else:
                            for i in range(len(list_obat["Riwayat Penyakit"])):
                                print(f"{i + 1}. Riwayat Penyakit: {list_obat['Riwayat Penyakit'][i]}, Resep Obat: {list_obat['Resep Obat'][i]}")
                            hapus_data = int(input("Resep obat nomor berapa yang ingin anda hapus: ")) - 1

                            if hapus_data < 0 or hapus_data >= len(list_obat["Riwayat Penyakit"]):
                                print("Tidak ada resep obat yang dimaksud, mohon input ulang.\n")
                            else:
                                print("Apa anda yakin ingin menghapus resep obat ini?")
                                print("1. Iya")
                                print("2. Tidak")
                                konfirmasi = input("Pilih: ")

                                if konfirmasi == "1":
                                    del list_obat["Riwayat Penyakit"][hapus_data]
                                    del list_obat["Resep Obat"][hapus_data]
                                    print("Resep obat berhasil dihapus.\n")
                                elif konfirmasi == "2":
                                    print("Hapus dibatalkan.")
                                else:
                                    print("Mohon pilih '1' atau '2'")

                    elif opsi == "5":
                        print("Logout berhasil. Terima kasih!\n")
                        pengguna_saat_ini = None  
                        break
                    else:
                        print("Input tidak valid, silahkan pilih 1, 2, 3, 4, atau 5.\n")

        elif opsi == "3":
            print("Terima kasih sudah menggunakan aplikasi ini. Semoga cepat sembuh!")
            break
        else:
            print("Input tidak valid, silahkan pilih 1, 2, atau 3.\n")


if __name__ == "__main__":
    main()