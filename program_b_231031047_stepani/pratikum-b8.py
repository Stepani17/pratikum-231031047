import os
os.system('clear')

pwd_benar = 'si23b'
a = True
i = 0
limit = 3

while a:
    i += 1
    pwd = input ('Masukan Password')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password Salah,!')
        if i <= limit:
            a = False
            print('Anda kehabisan kesempatan')
        else:
            print(f'Kesempatan anda tersisa {limit-i} kali')

#Komputer memilih angka [1...5]
#User tebak angka:
#jika salah 1: Tebakan salah, anda memiliki 2 kesempatan lagi
#jika salah 1: Tebakan salah, anda memiliki 1 kesempatan lagi
#jika salah 1: Tebakan salah, anda berhasil 
 #               Angka yang dicari adalah x

#jika benar: Anda Benar angka yang ditebak adalah x (Program selesai)

        
   
        