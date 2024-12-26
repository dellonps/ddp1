import tkinter as tk
from tkinter import Menu, scrolledtext
from tkinter import messagebox
import random
import time

# membuat kondisi-kondisi default
is_dark_mode = False # lightmode
correct_answer = None
xyz_mode = False

# fungsi untuk kirim pesan
def send_message():
    global correct_answer, xyz_mode
    user_message = entry.get()

    if user_message.strip(): # memastikan inputan bukan spasi kosong
        chat_display.configure(state="normal")
        chat_display.insert(tk.END, f"User: {user_message}\n") # input chat dari user

        # memproses berdasarkan mode yg dipilih user
        if xyz_mode: # mode hitung kata
            word_count = len(user_message.split())
            chat_display.insert(tk.END, f"Chatbot: Kalimat Anda memiliki {word_count} kata.\n")
            xyz_mode = False #kembali set menjadi default
        elif correct_answer is not None:
            check_answer() #panggil fungsi
            correct_answer = None #kembali set menjadi default
        else:
            chat_display.insert(tk.END, "Chatbot: Maaf, saya belum mengerti pertanyaan itu. Bisa coba yang lain!\n")

        # scroll ke paling akhir dan disable chat 
        chat_display.yview(tk.END)
        chat_display.configure(state="disabled")
        
        # kosongin field inputan
        entry.delete(0, tk.END)

# fungsi buat lelucon
def buat_lelucon():
    list_lelucon = [
        "Chatbot: Sayur apa yang pintar nyanyi? Kolplay!",
        "Chatbot: Kenapa ginjal ada dua?. Karena kalau satu ganjil!",
        "Chatbot: Gula, gula apa yang bukan gula? Gula aren’t!"
    ]
    chat_display.configure(state="normal")
    chat_display.insert(tk.END, "User: buat lelucon\n")

    def tampilkan_lelucon():
        lelucon = random.choice(list_lelucon)
        chat_display.insert(tk.END, lelucon + "\n")
        chat_display.configure(state="disabled")
        chat_display.yview(tk.END)

    root.after(1000, tampilkan_lelucon)

# fungsi tanya jam
def tanya_jam():
    chat_display.configure(state="normal")
    chat_display.insert(tk.END, "User: tanya jam\n")

    def tampilkan_jam():
        chat_display.insert(tk.END, f"Chatbot: Saat ini pukul {time.strftime('%H:%M:%S')}.\n")
        chat_display.configure(state="disabled")
        chat_display.yview(tk.END)

    root.after(1000, tampilkan_jam)

# fungsi soal mtk
def soal_matematika():
    global correct_answer
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    correct_answer = num1 + num2

    chat_display.configure(state="normal")
    chat_display.insert(tk.END, f"Chatbot: Berapa {num1} + {num2}?\n")
    chat_display.configure(state="disabled")
    chat_display.yview(tk.END)

# check jawaban mtk
def check_answer():
    global correct_answer
    try:
        user_answer = int(entry.get())
        if user_answer == correct_answer:
            chat_display.insert(tk.END, "Chatbot: Benar! Jawaban kamu tepat.\n")
        else:
            chat_display.insert(tk.END, f"Chatbot: Salah. Jawaban yang benar adalah {correct_answer}.\n")
    except ValueError:
        chat_display.insert(tk.END, "Chatbot: Masukkan angka yang valid!\n")

# fungsi hitung kata
def xyz_action():
    global xyz_mode
    xyz_mode = True
    chat_display.configure(state="normal")
    chat_display.insert(tk.END, "Chatbot: Silakan ketik sebuah kalimat, dan saya akan menghitung jumlah katanya.\n")
    chat_display.configure(state="disabled")
    chat_display.yview(tk.END)

# fungsi simpan sesi
def save_session():
    chat_content = chat_display.get("1.0", tk.END).strip()
    if chat_content == "Chatbot: Halo! Ada yang bisa saya bantu?":
        messagebox.showwarning("Info", "Tidak ada sesi untuk disimpan.")
        return

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"chat_session_{timestamp}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(chat_content)
        messagebox.showinfo("Sukses", f"Chat sesi berhasil disimpan sebagai {filename}.")
    except Exception as e:
        messagebox.showerror("Error", f"Gagal menyimpan sesi: {str(e)}")

# fungsi reset sesi
def reset_session():
    global correct_answer, xyz_mode
    correct_answer = None
    xyz_mode = False
    chat_display.configure(state="normal")
    chat_display.delete("1.0", tk.END)
    chat_display.insert(tk.END, "Chatbot: Halo! Ada yang bisa saya bantu?\n")
    chat_display.configure(state="disabled")
    messagebox.showinfo("Reset Sesi", "Sesi telah direset.")

# fungsi ganti tema
def switch_theme():
    global is_dark_mode
    if is_dark_mode:
        root.config(bg="white")
        chat_display.config(bg="white", fg="black", insertbackground="black")
        entry.config(bg="white", fg="black", insertbackground="black")
        is_dark_mode = False
    else:
        root.config(bg="black")
        chat_display.config(bg="black", fg="white", insertbackground="white")
        entry.config(bg="black", fg="white", insertbackground="white")
        is_dark_mode = True

# main app
root = tk.Tk()
root.title("Chatbot Sederhana")
root.geometry("500x400")
root.minsize(400, 300)

# membuat menu bar
menu_bar = Menu(root)
root.config(menu=menu_bar)

# menu file
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Simpan Sesi", command=save_session)
file_menu.add_command(label="Reset Sesi", command=reset_session)
file_menu.add_separator()
file_menu.add_command(label="Keluar", command=root.quit)
menu_bar.add_cascade(label="File", menu=file_menu)

# menu theme
theme_menu = Menu(menu_bar, tearoff=0)
theme_menu.add_command(label="Ubah Tema", command=switch_theme)
menu_bar.add_cascade(label="Tema", menu=theme_menu)

# menu tentang aplikasi
about_menu = Menu(menu_bar, tearoff=0)
about_menu.add_command(
    label="Tentang Aplikasi",
    command=lambda: messagebox.showinfo(
        "Tentang Aplikasi",
        "Aplikasi Chatbot ini dikembangkan oleh Cristian Dillon Philber dari FASILKOM UI di tahun 2024.\n"
        "Semoga aplikasi ini dapat menjadi pembelajaran yang bermanfaat!"
    )
)
menu_bar.add_cascade(label="Tentang", menu=about_menu)

# chat
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, height=15)
chat_display.configure(state="normal")
chat_display.delete("1.0", tk.END)
chat_display.insert(tk.END, "Chatbot: Halo! Ada yang bisa saya bantu?\n")
chat_display.configure(state="disabled")
chat_display.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

# button
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

joke_button = tk.Button(button_frame, text="Buat Lelucon", command=buat_lelucon)
joke_button.grid(row=0, column=0, padx=5)

time_button = tk.Button(button_frame, text="Tanya Jam", command=tanya_jam)
time_button.grid(row=0, column=1, padx=5)

math_button = tk.Button(button_frame, text="Soal Matematika", command=soal_matematika)
math_button.grid(row=0, column=2, padx=5)

xyz_button = tk.Button(button_frame, text="Hitung Kata", command=xyz_action)
xyz_button.grid(row=0, column=3, padx=5)

# frame
input_frame = tk.Frame(root)
input_frame.pack(pady=10)

input_frame.columnconfigure(0, weight=1)
input_frame.columnconfigure(1, weight=0)

# kotak input
entry = tk.Entry(input_frame, width=50)
entry.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

# button kirim
send_button = tk.Button(input_frame, text="Kirim", command=send_message)
send_button.grid(row=0, column=1, padx=5, pady=5)
root.bind("<Return>", lambda event: send_message())

# jalankan aplikasi
root.mainloop()