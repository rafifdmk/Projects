import time,os,sys

os.system('cls') #clear

print('A : halo kamu!\n\
A : perkenalkan nama saya Paijo, sebelumnya bisa berkenalan?')
time.sleep(1)
name=input('B : perkenalkan nama saya ')

print('A : salam kenal',name, ',apa kabar kamu?')
time.sleep(1)
myOne=input('B : kabar saya ')

print('A : saya akan memberikan pertanyaan seputar sekolah di smk telkom malang dan jawab dengan fakta ya',name)
time.sleep(1)
myOne=input('B : ')

print('A : asal SMP/Mts sebelum sekolah di smk telkom malang?')
time.sleep(1)
myOne=input('B : di ')

print('A : kamu di malang ini tinggal di? (kost/rumah)')
time.sleep(1)
tempat=input('B : saya di malang tinggal di ')

print('A : berapa jarak',tempat,name, 'ke sekolah?')
time.sleep(2)
myOne=input('B : sekitar ')

print('A :' ,name,'pergi sekolah menggunakan transportasi? (jalan kaki/motor/sepeda)')
time.sleep(1)
yaa=input('B : ')

if yaa=="jalan kaki":
    print('A : berapa lama perjalanan dari', tempat, 'ke sekolah dengan berjalan kaki?')
    time.sleep(1)
    input('B : sekitar ')
    print('A : jika berangakat sekolah bersama teman atau sendiri? (bersama teman/snediri)')
    time.sleep(1)
    input('B : jika berangkat sekolah biasanya ')
    print('A : sedangkan waktu pulang sekolah? (bersama teman/sendiri)')
    time.sleep(1)
    input('B : sedangkan pulang sekolah saya biasanya ')
    print('A : jika ada teman yang mengajak pulang menggunakan motor kamu akan? (tolak/terima)')
    time.sleep(1)
    input('B : saya akan ')
    
elif yaa=='motor':
    print('A : berapa lama perjalanan dari', tempat, 'ke sekolah dengan menggunakan motor?')
    time.sleep(1)
    input('B : sekitar ')
    print('A : jika berangkat sekolah menggunakan motor ananda', name, 'bersama teman?')
    time.sleep(1)
    input('B : ')
    print('A : ',name , 'pernah mengalami masalah di jalan saat menuju ke sekolah?')
    time.sleep(1)
    input('B : ')
    print('A : biaya yang di keluarkan untuk membeli bahan bakar untuk ke sekolah?')
    time.sleep(1)
    input('B : kurang lebih ')
    print('A : berapa hari sekali mengisi bahan bakar untuk ke sekolah?')
    time.sleep(1)
    input('B : ')
            
elif yaa=='sepeda':
    print('A : berapa lama perjalanan dari', tempat, 'ke sekolah dengan menggunakan sepeda?')
    time.sleep(1)
    input('B : sekitar ')
    print('A : apakah', name, ' berbocengan dengan teman saat berangkat sekolah? (iya/tidak)')
    time.sleep(1)
    input('B : ')
    print('A : sepeda yang di gunakan milik sendiri atau meminjam?')
    time.sleep(1)
    ee=input('B : ')
    
    if ee=='meminjam':
        print('A : jika meminjam, siapa pemilik sepeda itu?')
        input('B : ')

print('A : mata pelajaran yang', name, 'sukai?')
input('B : ')

print('A : dan mata pelajaran yang', name, 'tidak sukai?')
input('B : ')

print('A : guru favorit versi', name, '?')
input('B : ')

print('A : menurut', name, 'bagaimana peraturan yang sudah di buat oleh smk telkom malang? (sudah  baik/kurang baik)')
op=input('B : menurut saya ')

if op=='sudah baik':
    print('A : jika sudah baik, peraturan apa yang harus di tambah di sekolah?')
    input('B : ')

elif op=='kurang baik':
    print('A : jika kurang baik, apa yang yang harus di perbaiki dalam peratuaran sekolah?')
    input('B : ')
    
koki='A : baik....\n\
A : makasihh ananda yang sudah menjawab pertanyaan yang saya ajukan...\n\
A : dan juga sudah memberikan masukan kepada kita\n\
A : SAMPAI JUMPA LAGI DI LAIN WAKTU!!!!!!!!\n\
A : TENGKUYYYYYY!!!!!!!!!!!!!!'

def typewriter(koki):
    for char in koki:
         sys.stdout.write(char)
         sys.stdout.flush()
         
         if char !='/n':
             time.sleep(0.1)
         else:
            time.sleep(1)
            
typewriter(koki)