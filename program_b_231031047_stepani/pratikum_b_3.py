print('Pratikum-3 \n\n')
print('Nama Lengkap     : Stepani')
print('NIM              : 231031047')
print('Prodi            : Sistem Informasi')


print('pratikum-3')
a = True
b = False
print('=============AND==========')
hasil = not (a and a)
print(a,'nand',a,'adalah =',hasil)
hasil = not (a and b)
print (a,'nand',b,'adalah =',hasil)
hasil = not (b and a)
print (b,'nand',a,'adalah =',hasil)
hasil = not (b and b)
print(b,'nand',b,'adalah =',hasil)

print('=============NOR==========')
hasil = not (a and a)
print(a,'nor',a,'adalah =',hasil)
hasil = not (a and b)
print (a,'nor',b,'adalah =',hasil)
hasil = not (b and a)
print (b,'nor',a,'adalah =',hasil)
hasil = not (b and b)
print(b,'nor',b,'adalah =',hasil)

print('=============NXOR==========')
hasil = not (a ^ a)
print(a,'nxor',a,'adalah =',hasil)
hasil = not (a ^ b)
print (a,'nxor',b,'adalah =',hasil)
hasil = not (b ^ a)
print (b,'nxor',a,'adalah =',hasil)
hasil = not (b ^ b)
print(b,'nxor',b,'adalah =',hasil)

# INI OPERATOR MEMBERSHIP
print('\n========IN========')
nama = 'Stepani'
test = 'pa' #ISI dengan 2 huruf ada di nama
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test = 'ap' #ISI dengan 2 huruf ada di nama
cek  = test in nama
print(test,'ada di',nama,'adalah=',cek)

test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1,'ada di',nama,'adalah=',cek)

cek = test2 in nama
print(test2,'ada di',nama,'adalah=',cek)

cek = test3 in nama
print(test3,'ada di',nama,'adalah=',cek)

cek = test4 in nama
print(test4,'ada di',nama,'adalah=',cek)

cek = test5 in nama
print(test5,'ada di',nama,'adalah=',cek)

# INI Operator BITWISE
print('\n')
a = 17 #TAnggal lahir
b = 6 #Bulan Lahi
a+= 60
b+= 80
print('\n========AND=========')
print('Nilai',a,'biner adalah     =',format(a,'09b'))
print('Nilai',b,'biner adalah     =',format(b,'09b'))
print('----------------------------------AND')
c = a & b
print('Nilai',a,'&',b,'biner adalah= ',format(c,'09b'))

print('\n========OR=========')
#Tugas buat OR

print('========XOR=========')
#Tugas buat Xor

print('\n========NOT=========')
c = ~a
print('Nilai ',a,'biner adalah      =',format(a,'09b'))
print('Nilai not',a,'biner adalah   =',format(c,'09b'))
            
#tugas Lanjutakan untuk not b
c = ~b
print('Nilai ',b,'biner adalah      =',format(b,'09b'))
print('Nilai not',b,'biner adalah   =',format(c,'09b'))

print('\n========Left Shift=========')
c = a << 2
print('Nilai ',a,'biner adalah        =',format(a,'09b'))
print('Nilai ',a,'<< 2 biner adalah   =',format(c,'09b'))
c = b << 2
print('Nilai ',b,'biner adalah        =',format(b,'09b'))
print('Nilai ',b,'<< 2 biner adalah   =',format(c,'09b'))

print('\n========Right Shift=========')
c = a << 2
print('Nilai ',a,'biner adalah        =',format(a,'09b'))
print('Nilai ',a,'<< 2 biner adalah   =',format(c,'09b'))
c = b << 2
print('Nilai ',b,'biner adalah        =',format(b,'09b'))
print('Nilai ',b,'<< 2 biner adalah   =',format(c,'09b'))


print('\n========NOT AND=========')
# Tugas buat untuk nand

print('\n========NOT OR=========')
#Tugas buat NDR

print('\n========NOT XOR=========')
#Tugas buat NXOR
print('\n========NOT<< 2=========')
#Tugas buat untuk c =~(a<<2)
#Tugas buat untuk c =~(b<<2)
print('\n========NOT >> 2=========')
#Tugas


            



















