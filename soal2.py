nilai_1 = int(input("Masukan nilai ke-1 : "))
nilai_2 = int(input("Masukan nilai ke-2 : "))
nilai_3 = int(input("Masukan nilai ke-3 : "))

if nilai_1 < nilai_2 & nilai_3 :
    hasil = "nilai ke-1 lebih kecil dari bilangan ke-2 dan ke-3"
elif nilai_2 < nilai_1 & nilai_3 :
    hasil = "nilai ke-2 lebih kecil dari bilangan ke-1 dan ke-3"
elif nilai_3 < nilai_1 & nilai_2 :
    hasil = "nilai ke-3 lebih kecil dari bilangan ke-2 dan ke-1"

print(hasil)        
