import os , getpass
os.system("cls") #clear

produk=[]
harga = []
program="y"
user="admin"
password="1admin"

print("\tAPLIKASI LIST MODERN")
print("-----------------------------------\n")
inputUser=input("Masukan User :")
inputPass=getpass.getpass("Password     :")
print("\n-----------------------------------")

os.system("cls") #clear

if inputUser==user and inputPass==password:
    print("\tBACA SEBELUM LANJUT")
    print()
    print("PENTING!!!")
    print("1. Ketik tanda minus(-) di input berhenti\n   jika meng-akhiri program")
    print("2. Jika lanjut kosongkan dan enter di 'berhenti'")
    print("3. Masukan nama barang dan harga satu persatu")
    print()
    input("\t\t\t\tLanjut (enter)")

os.system('cls') #clear

while inputUser==user and inputPass==password:
    if program:
        print("---------------------------")
        print("1.input data")
        print("2.list")
        print("3.berhenti")
        print("---------------------------")
        pilihan=input("pilihan:")
        print("---------------------------")
        
        while pilihan=="1":
            os.system('cls') #clear
            #print(produk)
            inputProduk=input("Masukan produk : ")
            produk.append(inputProduk)
                
            #print(harga)
            inputHarga=input("Masukkan harga : ")
            harga.append(inputHarga)
                
            #print(list)
            print("---------------------------")
            print ("\tList Produk \n")
            
            x = 0
            while x < len(produk) :
                print(produk[x] + " = Rp " + harga[x])
                x = x + 1    
            print("---------------------------")
            stop=input("kembali       : ")
            print("---------------------------")

            #perintah berhenti
            if stop == "-":
                print("Produk sudah di input")
                print("---------------------------")
                break
            
        if pilihan=="2":
            os.system ('cls') #clear
            print("---------------------------")
            print("\tList Produk")
            print("---------------------------")
            for x in range(len(produk)):
                print (produk[x] +" = Rp " + harga[x])
                
        elif pilihan=="3":
            print("Terimakasih Sudah Menggunaka Aplikasi Kami:)")
            break
    
else:
    print("OPS USER ATAU PASSWORD ANDA SALAH!!")



    
#SUMBER REFRENSI    
#Modul python (Learn Python in One Day and Learn It Well_ Python for Beginners with Hands-on Project.
    #The only book you need to start coding in Python immediately ( PDFDrive ))
#latihan loop : https://youtu.be/szyfqq_whIg
#for loop : https://youtu.be/Z4qfMhx4XzQ
#while loop: https://youtu.be/ZupffvoCChQ
#break : https://youtu.be/B6scLunzn0I
#append : https://www.w3schools.com/python/python_variables.asp
#data list : Bu Bias