network = {}

def add_user(network, user):
    # cek apakah user dalam network
    if user not in network:
        network[user] = set()
        print(f"{user} berhasil ditambahkan sebagai user.\n")
    else:
        print(f"User {user} sudah terdaftar!\n")

def add_friend(network, user1, user2):
    # cek apakah user1 dan user2 dalam network
    if (user1 in network and user2 in network):
        network[user1].add(user2)
        network[user2].add(user1)
        print(f"Pertemanan {user1} dan {user2} berhasil ditambahkan.\n")
    else:
        print(f"User {user1} atau {user2} tidak terdaftar!\n")

def mutual_friends(network, user1, user2):
    # cek apakah user1 dan user2 dalam network
    if (user1 in network and user2 in network):
        #menggunakan intersect untuk cari irisan atau mutual friends
        mutual = network[user1].intersection(network[user2]) 
        if len(mutual) == 0:
            print(f"Tidak ada teman mutual antara {user1} dan {user2}.\n")
        else:
            print(f"Teman mutual dari {user1} dan {user2}: {mutual}\n")
    else:
        print(f"User {user1} atau {user2} tidak terdaftar!\n")

def suggest_friend(network, user):
    # cek apakah user dalam network
    if (user in network):
        suggestions = set()
        #loop teman dari user
        for friend in network[user]:
            # loop teman yang disarankan, yaitu teman-teman dari si teman (yg sedang di looping)
            for suggested_friend in network[friend]:
                # sarankan teman yang bukan teman dari user, dan juga bukan user itu sendiri
                if suggested_friend != user and suggested_friend not in network[user]:
                    suggestions.add(suggested_friend)
        # cek panjangnya, kalau 0, berarti ga ada teman yg disarankan
        if len(suggestions) == 0:
            print(f"Tidak ada teman yang dapat disarankan untuk {user} :(\n")
        # selain dari itu, artinya ada teman
        else:
            print(f"Teman yang disarankan untuk {user}: {suggestions}\n")
    else:
        print(f"User {user} tidak terdaftar!\n")

print("""
Selamat datang di PMB Friend! Berikut adalah menu yang dapat kamu pilih: 
1) Tambah user
2) Tambah pertemana
3) Cari teman mutual
4) Sarankan pertemanan
5) Keluar
""")

while True:
    opsi = input("Masukkan menu yang diinginkan (1-5): ")
    if opsi == "1":
        user = input("Masukkan nama user yang ingin ditambahkan: ")
        add_user(network, user)
    elif opsi == "2":
        user1 = input("Masukkan nama user pertama: ")
        user2 = input("Masukkan nama user kedua: ")
        add_friend(network,user1,user2)
    elif opsi == "3":
        user1 = input("Masukkan nama user pertama: ")
        user2 = input("Masukkan nama user kedua: ")
        mutual_friends(network,user1,user2)
    elif opsi == "4":
        user = input("Nama user yang ingin disarankan pertemanannya: ")
        suggest_friend(network, user)
    else:
        print("Terima kasih telah berkunjung ke PMB Friend!")
        break
