Nama = input("Masukkan Nama: ")
NIM = input("Masukkan NIM: ")

print("Halo, Selamat Datang", Nama)
print("NIM Kamu adalah", NIM)

while True:
    gaji_kerja = int(input('Masukkan Gaji Per Jam: '))
    jam_kerja = int(input('Masukkan Jam Kerja: '))
    
    total_gaji = jam_kerja * gaji_kerja
    
    if jam_kerja > 160:
        bonus = total_gaji * 0.1
        total_gaji += bonus
        print(f"Anda Mendapatkan Bonus: {bonus}")
        print(f"Total gaji (termasuk bonus): {total_gaji}")
    else:
        print("Anda Tidak Mendapatkan Bonus")
        print(f"Total gaji: {total_gaji}")
    
   if input("Apakah anda ingin menghitung ulang gaji? (iya/tidak): ") !="iya":
        print("Terima kasih, program selesai")
        break
