def bukafile(nama_file): # fungsi untuk membuka textfile
    read = ""
    f = open(nama_file)
    for i in f:
        read += i
    return read

def is_valid_DNA(pattern): #mengecek pattern apakah sebuah nukelotida atau tidak 
    nukleotida = ['A', 'G', 'T', 'C']
    isValid = True
    for char in pattern:
        if char not in nukleotida:
            isValid = False
    return isValid
        
def reverse_pattern(pattern): #fungsi untuk mengubah suatu strand menjadi komplementernya dan me-reverse strand
    result = ""
    for i in range(len(pattern), 0, -1):
        if(pattern[i-1] == 'A'):
            result += ('T')
        elif(pattern[i-1] == 'T'):
            result += ('A')
        elif(pattern[i-1] == 'G'):
            result += ('C')
        elif(pattern[i-1] == 'C'):
            result += ('G')
    return result

def count_k_mer(genome, pattern): #fungsi untuk menghitung berapa banyak k-mer dalam suatu genome baik strand tersebut maupun kreverse complement-nya
    count = 0
    for i in range(len(genome) - len(pattern) + 1):
        if (genome[i:i+len(pattern)] == pattern) or (genome[i:i+len(pattern)] == reverse_pattern(pattern)):
            count += 1
    return count

def frequent_k_mer(genome, k): #fungsi menghitung banyak k_mer dan reverse_k_mer ke dalam suatu list dan menampilkan k_mer terbanyak yang muncul 
    k_mers = []
    counts = []

    for i in range(len(genome) - k + 1):
        k_mer = genome[i:i+k]
        rev_k_mer = reverse_pattern(k_mer)
       
        if k_mer in k_mers:
            counts[k_mers.index(k_mer)] += 1
        else:
            k_mers.append(k_mer)
            counts.append(1)

        if rev_k_mer in k_mers:
            counts[k_mers.index(rev_k_mer)] += 1
        else:
            k_mers.append(rev_k_mer)
            counts.append(1)

    max_count = max(counts) #menentukan nilai terbesar di list counts

    frequent_k_mers = [] #inisiasi list kosong untuk memasukan kmer dengan count terbanyak
    for i in range(len(k_mers)):
        if counts[i] == max_count:
            frequent_k_mers.append(k_mers[i])

    return frequent_k_mers
            
while True:
    file = input("Genome file name: ") 
    try:
        read_file = bukafile(file)
        break
    except FileNotFoundError:
        print(f'File "{file}" tidak ditemukan. Coba lagi.')

opsi = input("""
Choose an option:
[1] Compute a reverse complement of a k-mer pattern
[2] Count a k-mer pattern
[3] Find most frequent k-mer patterns
Select an operation [1/2/3]: """)

if (opsi == "1"):
    while True :
        pattern = input("Input your pattern: ").upper()
        if is_valid_DNA(pattern) is False:
            print ("Inputan tidak valid, inputan harus berupa nukleotida, yaitu A/G/T/C")
            continue
        else:
            print(reverse_pattern(pattern))
            break

elif (opsi == "2"):
    while True :
        pattern = input("Input your pattern: ").upper()
        if is_valid_DNA(pattern) is False:
            print ("Inputan tidak valid, inputan harus berupa nukleotida, yaitu A/G/T/C")
            continue
        else:
            print(count_k_mer(read_file,pattern))
            break

    
elif (opsi == "3"):
    while True:
        try:
            k = int(input("Input your value of k: "))
            if k > 0:
                break
            else:
                print('"k" harus lebih dari 0')
        except ValueError:
            print('Inputan tidak valid, "k" harus berupa angka')

    for i in frequent_k_mer(read_file, k):
        print(i)