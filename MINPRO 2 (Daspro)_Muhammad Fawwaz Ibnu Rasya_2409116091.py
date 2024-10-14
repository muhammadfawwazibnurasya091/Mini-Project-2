#Data awal Akun 
akun = [
    {"Username": "Fawwaz", "Password": "Fawwaz22345", "Role": "Admin"},  # Perbaikan 'Passwprd' jadi 'Password'
    {"Username": "Pawas", "Password": "Pawas22345", "Role": "Pemesan"}
]

#Data Awal Permainan Tradisional
permainan = [
    {"nama": "Enggrang", "harga": "150.000", "deskripsi": "Permainan yang berbahan dasar Kayu atau Bambu yang kokoh sehingga bisa menjaga keseimbangan sang pengguna ketika dipakai berjalan atau berlari."},
    {"nama": "Bakiak", "harga": "120.000", "deskripsi": "Permainan Trafdisional yang menggunakan sebuah papan panjang dan lebar seukuran telapak kaki dan menggunakan karet ban untuk menopang kayu agar bisa dipakai secara bersama sama dengan teman/kerabat."},
    {"nama": "Gasing Kayu dan Tali", "harga": "80.000", "deskripsi": "Sebuah permainan tradisional seperti gasing modern, perbedaan nya hanya berbahan dasar kayu yang bernama kayu Ulin/Bengris, dan seutas tali."},
    {"nama": "Congklak", "harga": "200.000", "deskripsi": "Sebuah Permainan Tradisional yang menggunakan Kayu yang sudah di bolongi menjadi beberapa kolom dengan menggunakan Cangkang Kerang."}
]

#Data Awal Paket Permainan Tradisional
paket_permainan = [
    {
        "nama_paket": "Paket All In",
        "deskripsi_paket": "Paket ini berisi semua jenis Permainan Tradisional dengan jumlah yang lebih banyak. Include 5 Pasang Enggrang, 5 Pasang Bakiak, 10 Buah Gasing Kayu beserta tali gasingnya, dan 2 pasang Congklak.",
        "harga_paket": "2.500.000",
        "permainan": permainan  #Mengambil semua permainan tradisional yang ada
    }
]

#Fungsi umum
def tampilkan_daftar(daftar, jenis):
    if not daftar:
        print(f"Belum ada {jenis} yang tersedia.")
    else:
        print(f"\n=== Daftar {jenis} ===")
        for i, item in enumerate(daftar):
            if 'nama' in item:
                print(f"{i+1}. {item['nama']}, Harga: {item['harga']}, Deskripsi: {item['deskripsi']}")
            elif 'nama_paket' in item:
                print(f"{i+1}. {item['nama_paket']}, Harga: {item['harga_paket']}, Deskripsi: {item['deskripsi_paket']}")
                print("  Permainan dalam paket:")
                for p in item['permainan']:
                    print(f"    - {p['nama']}")

#Fungsi role Admin
def menu_admin():
    while True:
        print("\n=== Menu Admin ===")
        print("1. Tambah Permainan")
        print("2. Tambah Paket Permainan")
        print("3. Lihat Daftar")
        print("4. Update")
        print("5. Hapus")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            tambah_item(permainan, "permainan")
        elif pilihan == '2':
            tambah_paket()
        elif pilihan == '3':
            tampilkan_daftar(permainan, "Permainan")
            tampilkan_daftar(paket_permainan, "Paket")
        elif pilihan == '4':
            update_item()
        elif pilihan == '5':
            hapus_item()
        elif pilihan == '6':
            break
        else:
            print("Pilihan tidak valid")

def tambah_item(daftar, jenis):
    nama = input(f"Masukkan nama {jenis}: ")
    harga = input(f"Masukkan harga sewa {jenis}: ")
    deskripsi = input(f"Masukkan deskripsi {jenis}: ")
    daftar.append({"nama": nama, "harga": harga, "deskripsi": deskripsi})
    print(f"{jenis.capitalize()} {nama} berhasil ditambahkan.")

def tambah_paket():
    nama_paket = input("Masukkan nama paket permainan: ")
    deskripsi_paket = input("Masukkan deskripsi paket: ")
    harga_paket = input("Masukkan harga sewa paket: ")
    tampilkan_daftar(permainan, "Permainan")
    pilihan = input("Masukkan nomor permainan (pisahkan dengan koma): ")
    pilihan = [int(i) - 1 for i in pilihan.split(',') if i.strip().isdigit()]
    permainan_dalam_paket = [permainan[i] for i in pilihan if 0 <= i < len(permainan)]
    paket_permainan.append({"nama_paket": nama_paket, "deskripsi_paket": deskripsi_paket, "harga_paket": harga_paket, "permainan": permainan_dalam_paket})
    print(f"Paket {nama_paket} berhasil ditambahkan.")

def update_item():
    tampilkan_daftar(permainan, "Permainan")
    tampilkan_daftar(paket_permainan, "Paket")
    pilihan = input("Update (permainan/paket): ").lower()
    if pilihan == "permainan":
        update_permainan()
    elif pilihan == "paket":
        update_paket()
    else:
        print("Pilihan tidak valid.")

def update_permainan():
    nomor = int(input("Masukkan nomor permainan yang ingin diupdate: ")) - 1
    if 0 <= nomor < len(permainan):
        for key in ['nama', 'harga', 'deskripsi']:
            baru = input(f"Masukkan {key} baru (tekan enter jika tidak ingin mengubah): ")
            if baru:
                permainan[nomor][key] = baru
        print("Permainan berhasil diupdate.")
    else:
        print("Nomor permainan tidak valid.")

def update_paket():
    nomor = int(input("Masukkan nomor paket yang ingin diupdate: ")) - 1
    if 0 <= nomor < len(paket_permainan):
        for key in ['nama_paket', 'harga_paket', 'deskripsi_paket']:
            baru = input(f"Masukkan {key} baru (tekan enter jika tidak ingin mengubah): ")
            if baru:
                paket_permainan[nomor][key] = baru
        print("Paket berhasil diupdate.")
    else:
        print("Nomor paket tidak valid.")

def hapus_item():
    tampilkan_daftar(permainan, "Permainan")
    tampilkan_daftar(paket_permainan, "Paket")
    pilihan = input("Hapus (permainan/paket): ").lower()
    if pilihan == "permainan":
        hapus_permainan()
    elif pilihan == "paket":
        hapus_paket()
    else:
        print("Pilihan tidak valid.")

def hapus_permainan():
    nomor = int(input("Masukkan nomor permainan yang ingin dihapus: ")) - 1
    if 0 <= nomor < len(permainan):
        permainan_hapus = permainan.pop(nomor)
        print(f"Permainan {permainan_hapus['nama']} berhasil dihapus.")
    else:
        print("Nomor permainan tidak valid.")

def hapus_paket():
    nomor = int(input("Masukkan nomor paket yang ingin dihapus: ")) - 1
    if 0 <= nomor < len(paket_permainan):
        paket_hapus = paket_permainan.pop(nomor)
        print(f"Paket {paket_hapus['nama_paket']} berhasil dihapus.")
    else:
        print("Nomor paket tidak valid.")

#Fungsi role Pemesan
def menu_pemesan():
    while True:
        print("\n=== Menu Pemesan ===")
        print("1. Lihat Daftar")
        print("2. Pesan Permainan")
        print("3. Pesan Paket")
        print("4. Keluar")
        
        pilihan = input("Pilih menu: ")
        if pilihan == '1':
            tampilkan_daftar(permainan, "Permainan")
            tampilkan_daftar(paket_permainan, "Paket")
        elif pilihan == '2':
            pesan_permainan()
        elif pilihan == '3':
            pesan_paket()
        elif pilihan == '4':
            break
        else:
            print("Pilihan tidak valid")

def pesan_permainan():
    tampilkan_daftar(permainan, "Permainan")
    nomor = int(input("Masukkan nomor permainan yang ingin dipesan: ")) - 1
    if 0 <= nomor < len(permainan):
        print(f"Anda telah memesan {permainan[nomor]['nama']} dengan harga {permainan[nomor]['harga']}. Terima kasih!")
    else:
        print("Nomor permainan tidak valid.")

def pesan_paket():
    tampilkan_daftar(paket_permainan, "Paket")
    nomor = int(input("Masukkan nomor paket yang ingin dipesan: ")) - 1
    if 0 <= nomor < len(paket_permainan):
        print(f"Anda telah memesan paket {paket_permainan[nomor]['nama_paket']} dengan harga {paket_permainan[nomor]['harga_paket']}. Terima kasih!")
    else:
        print("Nomor paket tidak valid.")

#Login
def login():
    print("Sistem Login")
    while True:  # Ganti rekursi dengan loop
        Username = input("Masukkan Username: ")
        Password = input("Masukkan Password: ")
        
        #Cek Apakah Sudah Sesuai dengan Username dan Password
        user = next((u for u in akun if u['Username'] == Username and u['Password'] == Password), None)
        
        if user:
            print(f"Login berhasil! Anda masuk sebagai {user['Role'].capitalize()}.")
            if user["Role"] == "Admin":
                menu_admin()
            elif user["Role"] == "Pemesan":
                menu_pemesan()
            break  # Keluar dari loop jika login berhasil
        else:
            print("Username atau password salah. Silakan coba lagi.")

#Jalankan program
if __name__ == "__main__":
    login()
