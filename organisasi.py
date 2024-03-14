print('=' * 22)
print(" Masukan Biodata Anda")
print('=' * 22)

nama = input("Nama :")
jk = input("Jenis Kelamin :")
nilai = int(input('Nilai Rata-Rata akademis :'))
umur = int(input('Umur :'))
skil = input('Keahlian :')
bb = int(input('Berat Badan :'))
tb = int(input('Tinggi Badan :'))
sakit = input('Apakah anda punya penyakit cacat :')

if (jk == 'laki-laki' or 'perempuan') and (nilai >= 90) and (umur < 30) and (sakit == 'tidak') :
    hasil = 'Anda di terima di organisasi'
elif (jk == 'laki-laki' or 'perempuan') and (skil == 'berkuda' or 'menembak' or 'memanah') and (sakit == 'tidak') :
    hasil = 'Anda di terima di organisasi' 
elif (jk == 'laki-laki') and (bb <= 70) and (tb >= 170) and (umur <= 25) and (sakit == 'tidak'):
    hasil = 'Anda di terima di organisasi'
elif (jk == 'perempuan') and (bb >= 45 or bb <=50) and (tb >= 165) and (umur <20) and (sakit == 'tidak') :
    hasil = 'Anda di terima di organisasi'
else :
    print('Mohon Maaf anda tidak dapat di terima di organisasi')

print('Selamat', hasil)

