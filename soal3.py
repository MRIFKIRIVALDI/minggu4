nilai_1 = int(input("Masukan nilai ke-1 : "))
nilai_2 = int(input("Masukan nilai ke-2 : "))
nilai_3 = int(input("Masukan nilai ke-3 : "))

if nilai_1 == nilai_2 == nilai_3 :
    hasil = "ketiga nilai sama besar"
elif nilai_1 & nilai_2 > nilai_3 :
    hasil = "nilai 1 dan 2 lebih besar sari nilai 3"
elif nilai_2 & nilai_3 > nilai_1 :
    hasil = "nilai 2 dan 3 lebih besar sari nilai 1"
elif nilai_1 & nilai_3 > nilai_2 :
    hasil = "nilai 1 dan 3 lebih besar sari nilai 2"


print(hasil)  