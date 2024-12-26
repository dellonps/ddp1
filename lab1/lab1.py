print(">>==============================================<<")
print("||                    $$$$                      ||")
print("||              WELCOME TO UIMart               ||")
print("||               Receipt Printer                ||")
print("||                    $$$$                      ||")
print(">>==============================================<<")
print()
# input data user 
nama_produk = input("Masukkan nama produk: ")
jumlah_produk = int(input("Jumlah produk: "))
harga_produk = int(input("Masukkan harga produk: "))
diskon_produk = int(input("Masukkan diskon (dalam persentase 1-100): "))
tangggal_kadarluwarsa = int(input("Kapan tanggal expirednya?: "))
bulan_kadarluwarsa = int(input("Kapan bulan expirednya?: "))
nama_bank = input("Masukkan nama bank: ")
saldo_awal = int(input("Masukkan saldo awal: "))
# menghitung berapa minggu dan hari sebelum tanggal expired 
bulan1 = bulan_kadarluwarsa - 9
hari1 = bulan1*30 + tangggal_kadarluwarsa - 1
minggu_expired = hari1//7
hari_expired = hari1%7
#menghitung saldo akhir setelah dikenakan diskon 
saldo_akhir = saldo_awal - ((harga_produk*jumlah_produk)*diskon_produk/100)
print()
print(">>==============================================<<")
print("||                    UIMart                    ||")
print(">>==============================================<<")
print()
#print hasil out put 
print("Serial Code: " + nama_produk.upper() + str(tangggal_kadarluwarsa) + str(bulan_kadarluwarsa) + str(jumlah_produk) + nama_bank.upper())
print(nama_produk + " sejumlah " + str(jumlah_produk) + " berhasil dibeli!")
print("Produk akan expired dalam " + str(minggu_expired) + " minggu dan " + str(hari_expired) + " hari. ")
print("Saldo " + nama_bank.upper() + " anda sisa Rp " + str(saldo_akhir) + ". ")