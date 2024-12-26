def unique_words(list_of_words): #mendefinisikan lagi daftar kata unik menjadi bentuk dalam lower-cased
    list_of_unique_words = []
    for i in list_of_words:
        if i.lower() not in list_of_unique_words:
            list_of_unique_words.append(i.lower())
    return list_of_unique_words


def count_words(word, words): #menghitung berapa banyak daftar kata unik 
    count = 0
    for i in words:
        if i.lower() == word.lower():
            count+=1
    return count

def word_freqs(ws, words): # menghitung berapa banyak kemunculan setiap kata pada list ws 
    word_frequencies = []
    for i in ws:
        word_frequencies.append(count_words(i,words))
    return word_frequencies

print(unique_words(["halo","haloH","AlLIh", "allih"]))

file_found = False
while not file_found: # mengeloop file inputan jika file tidak di temukan dengan metode try-except
    try:
        nama_file = input("nama file = ")
        with open(nama_file) as file:
            content = file.read()
            
            words = content.split()
            unique_ws = unique_words(words)
            freqs_ws = word_freqs(unique_ws, words)
            
            print("Daftar kata unik:")
            for (w, freq) in zip(unique_ws, freqs_ws):
                print(w, freq)
        file_found = True

    except FileNotFoundError:
        print("File tidak ditemukan. Ulangi lagi!")