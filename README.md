Nur Ihsan 2409116051 Sistem Informasi kelas B
![Flowchart Nur Ihsann](https://github.com/user-attachments/assets/844b908a-6cc3-433e-a40f-8485230ca38a)
![image](https://github.com/user-attachments/assets/be15715c-e748-46dd-ba8b-db50805baa67)
![image](https://github.com/user-attachments/assets/b9452014-719e-4005-89d3-d61d4f5843dd)
Kode 1-2 (Login):
Nama = input("Masukkan Nama: ")
NIM = input("Masukkan NIM: ")
Penjelasan: Meminta dan menyimpan nama dan NIM pengguna.
Kode 3-4 (Sambutan):
print("Halo, Selamat Datang", Nama)
print("NIM Kamu adalah", NIM)
Penjelasan: Mencetak sambutan dan menampilkan NIM pengguna.
Kode 5-7 (Awal Loop dan Input):
while True:
gaji_kerja = int(input('Masukkan Gaji Per Jam: '))
jam_kerja = int(input('Masukkan Jam Kerja: '))
Penjelasan: Memulai loop tak terbatas dan meminta input gaji per jam dan jam kerja.
Kode 8-9 (Perhitungan Gaji):
total_gaji = jam_kerja * gaji_kerja
    
if jam_kerja > 160:
Penjelasan: Menghitung total gaji dan memeriksa apakah jam kerja lebih dari 160.
Kode 10-13 (Perhitungan Bonus):
bonus = total_gaji * 0.1
total_gaji += bonus
print(f"Anda Mendapatkan Bonus: {bonus}")
print(f"Total gaji (termasuk bonus): {total_gaji}")
Penjelasan: Menghitung bonus, menambahkannya ke total gaji, dan mencetak hasilnya.
Kode 14-15 (Tanpa Bonus):
else:
print("Anda Tidak Mendapatkan Bonus")
print(f"Total gaji: {total_gaji}")
Penjelasan: Mencetak total gaji tanpa bonus jika jam kerja tidak lebih dari 160.
Kode 17-20 (Akhir Program):
lanjut = input("Hitung gaji lagi? (iya/tidak): ").
if lanjut != 'iya':
print("Terima kasih! Program selesai.")
break
Penjelasan: Menanyakan apakah pengguna ingin menghitung lagi. Jika tidak, program berakhir.
