inp = input('Masukkan suatu input: ')
if len(inp) != 3:
 print('Panjang string ', len(inp),'tidak sama dengan 3')
else:
 print('Panjang input sesuai yang diinginkan')

 inp = input('Masukan suatu input: ')

if len(inp) != 3:
    print('Panjang string', len(inp),'tidak sama dengan 3')

else:
    print('Panjang input sesuai yang diinginkan')

print()
nilai = int(input('Masukan nilai: '))

if nilai >= 95:
    print('Nilai huruf: A')
elif nilai > 70:
    print('Nilai huruf: B')
elif nilai > 65:
    print('Nilai huruf: C')
else:
    print('Nilai huruf: D')