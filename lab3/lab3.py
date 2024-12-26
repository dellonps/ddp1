def format_row_manual(kucing_str):
    nama_end = kucing_str.find('-')
    umur_end = kucing_str.find('-', nama_end + 1)
    jenis_end = kucing_str.find('-', umur_end + 1) 

    nama = kucing_str[:nama_end]
    umur = kucing_str[nama_end + 1:umur_end]
    jenis = kucing_str[umur_end + 1:jenis_end]
    warna = kucing_str[jenis_end + 1:]

    return "{:<9} | {:<4} | {:<18} | {:<8}".format(nama, umur, jenis, warna)

kucingITB = "Puss-2-British-Shorthair-Orange,Scar-5-Sphynx-White,Jelly-1-American Wirehair-Grey,Yawhi-3-Siamese-White,Mi-3-Munchkin-Orange,Anak-2-Angora-Black,Rav-6-Angora-Brown"
kucingUI = "Leon-2-Somali-Grey,Sa-2-American Curl-White,Panda-4-ExoticShorthair-Black,Lala-3-LaPerm-Black,Ninya-2-Somali-Beige,Vae-1-LaPerm-Grey,Rinny-4-Highlander-Grey"

universitas = int(input("""Selamat datang di DepeCat!
Berikut list universitas yang menyediakan adopsi kucing:
1) UI
2) ITB
Masukkan pilihan sesuai angka yang tertera di depan nama universitas: """))

if universitas == 1:
    pilihan = int(input("""\nSilakan pilih menu!
1) Cetak semua data kucing
2) Cari kucing

Pilihan: """))

    if pilihan == 1:
        print("{:<9} | {:<4} | {:<18} | {:<8}".format("Nama", "Umur", "Jenis", "Warna"))
        print("–---------|------|--------------------|----------|")
        for kucing in kucingUI.split(","):
            print(format_row_manual(kucing))

    if pilihan == 2:
        keyword = input("\nMasukkan kata kunci pencarian: ").lower()
        found = False
        urutan = 1
        for kucing in kucingUI.split(","):
            nama_end = kucing.find('-')
            umur_end = kucing.find('-', nama_end + 1)
            jenis_end = kucing.find('-', umur_end + 1)

            nama = kucing[:nama_end].lower()
            umur = kucing[nama_end + 1:umur_end].lower()
            jenis = kucing[umur_end + 1:jenis_end].lower()
            warna = kucing[jenis_end + 1:].lower()

            if (keyword in nama) or (keyword in umur) or (keyword in jenis) or (keyword in warna):
                print(f"Kucing ditemukan pada baris ke-{urutan}")
                found = True
                break
            urutan += 1

        if not found:
            print("Kata kunci tidak ditemukan!")

elif universitas == 2:
    pilihan = int(input("""\nSilakan pilih menu!
1) Cetak semua data kucing
2) Cari kucing

Pilihan: """))

    if pilihan == 1:
        print("{:<9} | {:<4} | {:<18} | {:<8}".format("Nama", "Umur", "Jenis", "Warna"))
        print("–---------|------|--------------------|----------|")
        for kucing in kucingITB.split(","):
            print(format_row_manual(kucing))

    if pilihan == 2:
        keyword = input("\nMasukkan kata kunci pencarian: ").lower()
        found = False
        urutan = 1
        for kucing in kucingITB.split(","):
            nama_end = kucing.find('-')
            umur_end = kucing.find('-', nama_end + 1)
            jenis_end = kucing.find('-', umur_end + 1)

            nama = kucing[:nama_end].lower()
            umur = kucing[nama_end + 1:umur_end].lower()
            jenis = kucing[umur_end + 1:jenis_end].lower()
            warna = kucing[jenis_end + 1:].lower()

            if (keyword in nama) or (keyword in umur) or (keyword in jenis) or (keyword in warna):
                print(f"Kucing ditemukan pada baris ke-{urutan}")
                found = True
                break
            urutan += 1

        if not found:
            print("Kata kunci tidak ditemukan!")

print("\nTerima kasih telah mengunjungi DepeCat!")
