import os
os.system('cls') #clear

print('\tMenu')
print('Tumbuhan : Mawar,Melati')
print('Buah     : Anggur,Jeruk,Apel')
print()
pilihan=input('Pilihan Anda : ')
print()

print('Waktu Penyiraman Perhari:')
print('Apel   : 1 kali')
print('Jeruk  : 2 kali')
print('Anggur : 4 kali')
print('Mawar  : 6 kali')
print('Melati : 7 kali')
print()
hari=int(input('Masukan jumlah hari : '))
print()
if pilihan=='apel':
    hasil=hari*1
    print('Total penyiraman :',hasil)
    
if pilihan=='jeruk':
    hasil1=hari*2
    print('Total penyiraman :',hasil1)
    
if pilihan=='anggur':
    hasil2=hari*4
    print('Total penyiraman :',hasil2)
    
elif pilihan=='mawar':
    hasil3=hari*6
    print('Total penyiraman :',hasil3)
    
elif pilihan=='melati':
    hasil4=hari*7
    print('Total penyiraman :',hasil4)