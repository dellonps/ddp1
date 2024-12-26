barang = []  # [(“Code1”,“ItemName1”), (“Code2”,“ItemName2”)]
stok = []    # [StokItem1, StokItem2]

def tambah_barang(code, itemName, stokItem):
    # cek ada barang atau ga
    for i in range(len(barang)): # cek apakah tupel ada di list barang
        if code == barang[i][0]:  
            print(f"\nGAGAL! Kode barang {code} sudah ada di dalam sistem.\n")
            return  # keluar fungsi kalau misalnya barang ditemukan
    barang.append((code, itemName))
    stok.append(stokItem)
    print(f"\nBERHASIL! Barang ({code}, {itemName}) berjumlah {stokItem} berhasil ditambahkan ke dalam storage.\n")

def kurangi_stok(code, jumlahKurang):
    for i in range(len(barang)): # cek apakah tupel ada di list barang
        if code == barang[i][0]:
            if stok[i] - jumlahKurang > 0:
                stok[i] -= jumlahKurang
                print(f"\nBERHASIL! Stok barang ID {code} tersisa {stok[i]}.\n")
            elif stok[i] - jumlahKurang < 0:
                print(f"\nGAGAL! Jumlah barang {code} tidak cukup.\n")
            elif stok[i] - jumlahKurang == 0:
                del barang[i]
                del stok[i]
                print(f"\nBERHASIL! Barang ID {code} dihapus dari sistem.\n")
            return  # keluar dari fungsi
    print(f"\nGAGAL! Kode barang tidak di dalam sistem.\n")

# program utama
while True:
    opsi = input("Masukkan Opsi yang diinginkan (T/K/Q): ")
    if opsi == "T":
        kode = input("Kode barang: ")
        nama = input("Nama barang: ")
        stok_barang = int(input("Stok barang: ")) 
        tambah_barang(kode, nama, stok_barang)
    elif opsi == "K":
        kode = input("Kode barang: ")
        jumlahKurang = int(input("Jumlah barang yang ingin dikurangi: "))
        kurangi_stok(kode, jumlahKurang)
    elif opsi == "Q":
        print("Bye-Bye!")
        break
    else:
        print("Opsi tidak valid. Pilih T, K, atau Q.")
