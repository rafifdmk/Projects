import os
os.system('cls') #clear

saldo='120.000.000'
nasabah='Yono'

bank1=11335
t1='Wiwin'

bank2=12345
t2='Yaya'

bank3=55111
t3='Opi'

print('===========================================')
print('\tSelamat Datang Di ATM KITA')
print('-------Mengutamakan Kepuasan Nasabah-------')
print('===========================================')

print('\t \tMENU ANDA')
print('===========================================')
print('1.Informasi Saldo Anda\n\
2.Tarik Saldo Anda\n\
3.Tambah Saldo Anda\n\
4.Transfer')

print('')    
s=input('Masukan Option Anda : ')

os.system('cls') #clear

if s=='1':
    print('==============================================')
    print('\t\tATM KITA')
    print('\tMengutamakan Kepuasan Nasabah')
    print('==============================================')
    print('')
    print('Dari Bank            : Kita')
    print('Nama Nasabah         :',nasabah)
    print('Saldo Anda Berjumlah :',saldo)
    print('')
    print('   Terimakasih Telah Menggunakan Jasa kita')
    print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
    print('==============================================')
    
elif s=='2':
    print('Saldo Saat Ini            :',saldo)
    print('==============================================')
    print('Saldo Yang Ingin Di Tarik :')
    print('1. Rp 100.000')
    print('2. Rp 200.000')
    print('3. Rp 500.000')
    print('4. Rp 1.000.000')
    print('')
    uang_kamu=120000000
    option=input("Opsion : ")
    
    os.system('cls') #claer
    
    if option=='1':
        hasil=uang_kamu-100000
        print('==============================================')
        print('\t\tATM KITA')
        print('\tMengutamakan Kepuasan Nasabah')
        print('==============================================')
        print('')
        print('Dari Bank                     : Kita')
        print('Nama Nasabah                  :',nasabah)
        print('Anda Manarik Saldo Sebesar    : 100.000')
        print("Saldo Anda Sekarang Berjumlah :",hasil)
        print('')
        print('   Terimakasih Telah Menggunakan Jasa kita')
        print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
        print('==============================================')
    
    elif option=='2':
          hasil2=uang_kamu-200000
          print('==============================================')
          print('\t\tATM KITA')
          print('\tMengutamakan Kepuasan Nasabah')
          print('==============================================')
          print('')
          print('Dari Bank                     : Kita')
          print('Nama Nasabah                  :',nasabah)
          print('Anda Manarik Saldo Sebesar    : 200.000')
          print("Saldo Anda Sekarang Berjumlah :",hasil2)
          print('')
          print('   Terimakasih Telah Menggunakan Jasa kita')
          print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
          print('==============================================')
    
    if option=='3':
        hasil3=uang_kamu-500000
        print('==============================================')
        print('\t\tATM KITA')
        print('\tMengutamakan Kepuasan Nasabah')
        print('==============================================')
        print('')
        print('Dari Bank                     : Kita')
        print('Nama Nasabah                  :',nasabah)
        print('Anda Manarik Saldo Sebesar    : 500.000')
        print("Saldo Anda Sekarang Berjumlah :",hasil3)
        print('')
        print('   Terimakasih Telah Menggunakan Jasa kita')
        print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
        print('==============================================')
    
    elif option=='4':
          hasil4=uang_kamu-1000000
          print('==============================================')
          print('\t\tATM KITA')
          print('\tMengutamakan Kepuasan Nasabah')
          print('==============================================')
          print('')
          print('Dari Bank                     : Kita')
          print('Nama Nasabah                  :',nasabah)
          print('Anda Manarik Saldo Sebesar    : 1.000.000')
          print("Saldo Anda Sekarang Berjumlah :",hasil4)
          print('')
          print('   Terimakasih Telah Menggunakan Jasa kita')
          print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
          print('==============================================')
    
if s=='3':
    uang_kamu=120000000
    print('Saldo Saat Ini :',saldo)
    print('==============================================')
    yui=int(input('Masukan Saldo\n\
Yang Ingin Di Tambah:'))
    hasil6=uang_kamu+yui
    os.system('cls') #clear
    print('==============================================')
    print('\t\tATM KITA')
    print('\tMengutamakan Kepuasan Nasabah')
    print('==============================================')
    print('')
    print('Dari Bank                     : Kita')
    print('Nama Nasabah                  :',nasabah)
    print('Anda Menambah Saldo Sebesar   :',yui)
    print("Saldo Anda Sekarang Berjumlah :",hasil6)
    print('')
    print('   Terimakasih Telah Menggunakan Jasa kita')
    print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
    print('==============================================')
    
if s=='4':
    print('==============================================')
    print('')
    print('1. Transfer Sesama Bank')
    print('2. Transfer Bank Lain')
    print('')
    print('==============================================')
    k=int(input('Option Yang Anda Pilih :'))
    print('==============================================')
    os.system('cls') #clear
    if k==1:
        print('==============================================')
        print('Masukan Nomer Rekening 5 Digit :')
        f=int(input())
        print('==============================================')
        if f==11335:
            uang_=120000000
            print('Masukan Nominal Yang Ingin Di Transfer :')
            bn=int(input())
            print('==============================================')
            hasil7=bn+5000
            hasil5=uang_-hasil7
            os.system('cls') #clear
            print('==============================================')
            print('\t\tATM KITA')
            print('\tMengutamakan Kepuasan Nasabah')
            print('==============================================')
            print('')
            print('Nama Tujuan         :',t1)
            print('Transfer Sebesar    :',bn)
            print('Biaya Transfer      : 5.000')
            print('Total Transfer      :',hasil7)
            print('')
            print('==============================================')
            input('\t\t\t\t\tENTER')
            print('==============================================')
            os.system('cls') #clear
            print('==============================================')
            print('\t\tATM KITA')
            print('\tMengutamakan Kepuasan Nasabah')
            print('==============================================')
            print('')
            print('Anda Telah Trasfer Sebesar :',hasil7)
            print('Sisa Saldo Anda Sekarang   :',hasil5)
            print('')
            print('   Terimakasih Telah Menggunakan Jasa kita')
            print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
            print('==============================================')
        else:
            print('   Nomer Rekining Yang Anda Masukan Salah!!')
    
    elif k==2:
        print('==============================================')
        print('\t\tKODE BANK LAIN')
        print('Bank 1 : 101')
        print('Bank 2 : 118')
        print('==============================================')
        print('Masukan Kode Bank Beserta Rekening :')
        w=int(input())
        if w==10112345:
            uang1=120000000
            print('Masukan Nominal Yang Ingin Di Transfer :')
            tr=int(input())
            print('==============================================')
            hasil8=tr+7000
            hasil9=uang1-hasil8
            os.system('cls') #clear
            print('==============================================')
            print('\t\tATM KITA')
            print('\tMengutamakan Kepuasan Nasabah')
            print('==============================================')
            print('')
            print('Nama Tujuan         :',t2)
            print('Transfer Sebesar    :',tr)
            print('Biaya Transfer      : 7.000')
            print('Total Transfer      :',hasil8)
            print('')
            print('==============================================')
            input('\t\t\t\t\tENTER')
            print('==============================================')
            os.system('cls') #clear
            print('==============================================')
            print('\t\tATM KITA')
            print('\tMengutamakan Kepuasan Nasabah')
            print('==============================================')
            print('')
            print('Anda Telah Trasfer Sebesar :',hasil8)
            print('Sisa Saldo Anda Sekarang   :',hasil9)
            print('')
            print('   Terimakasih Telah Menggunakan Jasa kita')
            print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
            print('==============================================')
            
            
            if w==11855111:
                uang2=120000000
                print('Masukan Nominal Yang Ingin Di Transfer :')
                hp=int(input())
                print('==============================================')
                hasil11=hp+9000
                hasil00=uang2-hasil11
                os.system('cls') #clear
                print('==============================================')
                print('\t\tATM KITA')
                print('\tMengutamakan Kepuasan Nasabah')
                print('==============================================')
                print('')
                print('Nama Tujuan         :',t3)
                print('Transfer Sebesar    :',hp)
                print('Biaya Transfer      : 9.000')
                print('Total Transfer      :',hasil11)
                print('')
                print('==============================================')
                input('\t\t\t\t\tENTER')
                print('==============================================')
                os.system('cls') #clear
                print('==============================================')
                print('\t\tATM KITA')
                print('\tMengutamakan Kepuasan Nasabah')
                print('==============================================')
                print('')
                print('Anda Telah Trasfer Sebesar :',hasil11)
                print('Sisa Saldo Anda Sekarang   :',hasil00)
                print('')
                print('   Terimakasih Telah Menggunakan Jasa kita')
                print('Bank Kita selalu mengutamkan Kepuasan Nasabah')
                print('==============================================')
        else:
            print('==============================================')
            print('\tNomer Rekining/Kode Bank Salah!!')       