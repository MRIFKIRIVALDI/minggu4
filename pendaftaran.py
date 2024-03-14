print("masukan identitas anda")
nama = input("Nama : ")
tempat_Lahir = input("Tempat lahir :")
tahun_lahir = int(input("Tahun lahir :"))
jenis_kelamin = input("Jenis Kelamin :")

print(" Masukan nilai anda ")
english = int(input("Nilai englis :"))
mtk = int(input("Mtk :"))
indo = int(input("B. Indonesia :"))

rata2 = (english+mtk+indo)/3

if tahun_lahir <= 1999 :
    hasil = "Mohon maaf anda tidak dapat di terima di kampus ini"
elif rata2 >=80 and jenis_kelamin == "laki laki":
    hasil = "Anda di sarankan untuk masuk jurusan teknik informatika"
elif rata2 >=80 and jenis_kelamin == "perempuan":
    hasil = "Anda di sarankan untuk masuk jurusan sistem operasi"   
else :
    hasil = "Anda disarankan masuk jurusan DKV"

print(hasil)