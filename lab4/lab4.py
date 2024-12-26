def bukafile(nama_file):
    res = ""
    nomor = 1
    huruf = 0
    baris = 0
    with open(nama_file, 'r') as f:
        for line in f:
            res += f'{nomor:03d}. {line}'
            nomor += 1
            for char in line: #loop tiap karakter tiap line untuk cek apakah alfabet, jika alfabet, tambah huruf
                if ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
                    huruf +=1
            if line != "\n": #cek apakah baris tidak kosong, jika bukan baris kosong, tambah baris
                baris += 1
    res += f"\n\nTotal banyakya huruf = {huruf} huruf\n"
    res += f"Banyakya baris tidak kosong = {baris} baris" 
    return res

input_file = input("nama file input = ")
output_file = input("nama file output = ")

result = bukafile(input_file) #membuka file dan generate result
with open(output_file, 'w') as f_out: #write result dan membuat file baru dengan nama file yg sudah ditentukan.
    f_out.write(result)  

print(f"akhir program, silakan buka isi {output_file}")