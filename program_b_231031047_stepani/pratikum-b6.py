# Buat file python dengan nama pratikum-b6.py

# Buat program perulagan while dengan jumlah perulangan sebanyak 3 kali

import os
os.system('clear')

a = True
i = 0
limit = 3

while a:
    i +=1
    if i <= limit:
        print('Selamat Bergabung',limit-i+1)
    else:
        a = False