a = int(input("Masukan nilai a : "))
b = int(input("Masukan nilai b : "))
c = int(input("Masukan nilai c : "))

if a > b and a > c :
    hasil = "nilai a adalah nilai terbesar"
elif b > a and b > c :
    hasil = "nilai b adalah nilai terbesar"
elif c > a and c > b :
    hasil = "nilai c adalah nilai terbesar"
elif a == b and a > c :
    hasil = "nilai a dan b sama besar dan lebih besar dari c"
elif a == c and a > b :
    hasil = "nilai a dan c sama besar dan lebih besar dari b"
elif b == c and b > a :
    hasil = "nilai b dan c sama besar dan lebih besar dari a"   
else :
    hasil = "semua bilangan sama besar"            

print(hasil)        


