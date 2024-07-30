import os
os.system('cls') #clear

print('\t DAFTAR MENU\n\
Makanan: \t Minuman\n\
1. Nasi goreng \t 4. Air putih\n\
2. Nasi putih \t 5. Air soda\n\
3. Nasi rawon \t 6. Susu\n\
')


mkn=input('Masukan pilihan makanan anda : ')
mnm=input('Masukan pilihan minuman anda : ')

if mkn=='1':
    data_makan1='Nasi goreng'

if mkn=='2':
    data_makan1=('Nasi putih')
    
if mkn=='3':
    data_makan1=('Nasi rawon')

if mnm=='4':
    data_minum2=('Air putih')
    
if mnm=='5':
    data_minum2=('Air soda')
    
if mnm=='6':
    data_minum2=('susu')

p=input('\n\
Kasir   : ')
o=input('Pembeli : ')

print('\n\
\tNOTA\n\
Kasir   :',p,'\n\
Pembeli :',o,'\n\
\n\
Pesanan :')
print(data_makan1)
print(data_minum2)
print('\t \t Malang\n\
\t \t  2022')