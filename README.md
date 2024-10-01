Nur Ihsan 2409116051 Sistem Informasi kelas B
![Flowchart Nur Ihsann](https://github.com/user-attachments/assets/844b908a-6cc3-433e-a40f-8485230ca38a)
![image](https://github.com/user-attachments/assets/be15715c-e748-46dd-ba8b-db50805baa67)
![image](https://github.com/user-attachments/assets/b9452014-719e-4005-89d3-d61d4f5843dd)
Kode 1-2 (Login):
Nama = input("Masukkan Nama: ")
NIM = input("Masukkan NIM: ")
Penjelasan: 
1. Input Nama dan NIM:

Nama = input("Masukkan Nama: ")
NIM = input("Masukkan NIM: ")

Bagian ini meminta input dari pengguna untuk memasukkan nama dan NIM. Fungsi input() digunakan untuk membaca data yang dimasukkan oleh pengguna.

2. Menyapa pengguna:

print("Halo, Selamat Datang", Nama)
print("NIM Kamu adalah", NIM)

Setelah pengguna memasukkan nama dan NIM, program menyapa pengguna dengan menampilkan pesan "Halo, Selamat Datang" diikuti dengan nama, dan "NIM Kamu adalah" diikuti dengan NIM yang telah dimasukkan sebelumnya.

3. Perulangan (Looping):

while True:

Program masuk ke dalam perulangan tak terbatas (while True:). Ini berarti program akan terus mengulang sampai pengguna secara eksplisit menghentikannya dengan memilih untuk tidak menghitung ulang gaji di bagian bawah kode.

4. Input Gaji Per Jam dan Jam Kerja:

gaji_kerja = int(input('Masukkan Gaji Per Jam: '))
jam_kerja = int(input('Masukkan Jam Kerja: '))

Program meminta pengguna untuk memasukkan gaji per jam dan jumlah jam kerja yang mereka lakukan. Kedua input ini dikonversi menjadi tipe data int (integer) agar bisa digunakan dalam perhitungan matematis.

5. Menghitung Total Gaji:

total_gaji = jam_kerja * gaji_kerja

Program menghitung total gaji dengan mengalikan jumlah jam kerja (jam_kerja) dengan gaji per jam (gaji_kerja). Hasilnya disimpan dalam variabel total_gaji.

6. Mengecek Jam Kerja dan Menghitung Bonus (Jika Ada):

if jam_kerja > 160:
    bonus = total_gaji * 0.1
    total_gaji += bonus
    print(f"Anda Mendapatkan Bonus: {bonus}")
    print(f"Total gaji (termasuk bonus): {total_gaji}")
else:
    print("Anda Tidak Mendapatkan Bonus")
    print(f"Total gaji: {total_gaji}")

Program mengecek apakah jumlah jam kerja lebih dari 160 jam. Jika iya (if jam_kerja > 160:), maka pengguna akan mendapatkan bonus sebesar 10% dari total gaji (total_gaji * 0.1). Bonus ditambahkan ke total gaji, dan pesan yang menunjukkan jumlah bonus serta total gaji yang diperoleh ditampilkan.

Jika jam kerja tidak lebih dari 160 jam (else), program hanya menampilkan total gaji tanpa bonus.

7. Menanyakan Pengguna Apakah Ingin Menghitung Ulang:

if input("Apakah anda ingin menghitung ulang gaji? (iya/tidak): ") != "iya":
    print("Terima kasih, program selesai")
    break

Setelah menampilkan hasil perhitungan, program akan bertanya kepada pengguna apakah mereka ingin menghitung ulang gaji. Jika pengguna mengetikkan "iya", program akan mengulangi perhitungan. Jika tidak, program akan menampilkan pesan "Terima kasih, program selesai" dan perulangan akan dihentikan menggunakan perintah break.
