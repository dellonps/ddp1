import time
def partition_asc(A, p, r): # Fungsi partition untuk sorting ascending
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def partition_desc(A, p, r): # Fungsi partition untuk sorting descending
    pivot = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] >= pivot:  
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1

def quicksort_asc(A, p, r): # Fungsi QuickSort untuk ascending order
    if p < r:
        q = partition_asc(A, p, r) 
        quicksort_asc(A, p, q - 1)
        quicksort_asc(A, q + 1, r)

def quicksort_desc(A, p, r): # Fungsi QuickSort untuk descending order
    if p < r:
        q = partition_desc(A, p, r)
        quicksort_desc(A, p, q - 1)
        quicksort_desc(A, q + 1, r)

def main(): # Fungsi utama untuk menjalankan program
    print("""
CTP 03 DDP1 -- 2024
Implementation of QuickSort
============================""")
    try:  # Meminta input nama file dan metode sorting (ascending/descending)
        input_file = input("Input file name: ")
        output_file = input("Output file name: ")
        sort_style = input("(1) Ascending\n(2) Descending\n Pick what type of sort you like :  ")

        if sort_style == "1"  :

            int_array = []
            ifile = open(input_file)
            for line in ifile:
                int_array.append(int(line.strip()))
            
            t1 = time.time()
            t = time.process_time()

            print("Sorting in progress ...")
            quicksort_asc(int_array, 0, len(int_array) - 1)
            duration = time.time() - t1
            cpu_time = time.process_time() - t

        elif sort_style == "2" :
        
            int_array = []
            ifile = open(input_file)
            for line in ifile:
                int_array.append(int(line.strip()))
            
            t1 = time.time() # Waktu awal (real time)
            t = time.process_time() # Waktu awal (CPU time)

            print("Sorting in progress ...")
            quicksort_desc(int_array, 0, len(int_array) - 1)
            duration = time.time() - t1
            cpu_time = time.process_time() - t

        # Menyimpan hasil ke file output
        with open(output_file, 'w') as ofile:
            for i in int_array:
                ofile.write(str(i)+"\n")  # Tulis hasil sorting ke file
        
        ifile.close() # Tutup file input
        ofile.close() # Tutup file output

        print("CPU time of the quicksort: ", cpu_time)
        print("Clock time of the quicksort: ", duration)
    except FileNotFoundError:
        print("Input file error.")

if __name__ == '__main__': # Panggil fungsi main jika dijalankan sebagai script
    main()