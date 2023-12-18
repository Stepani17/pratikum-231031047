import os
os.system('clear')

a = True

while a:
    jawab = input('Apakah ingin lanjudkan?(y/n)')
    if jawab == 'y':
        os.system('clear')
        print('Selamat Datang lagi!')
    elif jawab == 'n':
        print('Sampai Ketemu Lagi :D')
        a = False
    else:
        print('Jangan aneh-aneh deh :.)')
        a = True
        