import random
bot = ['batu' , 'gunting' , 'kertas']

while True :
    x = random.choice(bot)
    data = input('Masukan pilihan anda :')
    if data.lower() == x :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Hasil seri \n\n")


        #bagian menang
    elif data.lower() == 'batu' and x == 'gunting' :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu menang \n\n")   

    elif data.lower() == 'kertas' and x == 'batu' :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu menang \n\n")      

    elif data.lower() == 'gunting' and x == 'kertas' :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu menang \n\n")  


        #bagian kalah
    elif data.lower() == 'gunting' and x == 'batu' :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Kalah \n\n")   

    elif data.lower() == 'batu' and x == 'kertas' :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Kalah \n\n")      

    elif data.lower() == 'kertas' and x == 'gunting' :
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Kalah \n\n")     

    else :
        print('data yang di masukan salah\n\n')    