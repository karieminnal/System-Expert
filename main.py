import os

print("+-----------------------------------------------+")
print("|\t\tSelamat Datang di Sistem Pakar\t\t\t|")
print("|\t\tDeteksi Gejala Magh dan Usus Buntu\t\t|")
print("+-----------------------------------------------+")
nama = input("Nama\t: ")
pilihan = input("\nHallo "+nama+" , \nApakah anda ingin melakukan diagnosa ? (y/n) : ")

os.system('clear')

while pilihan == 'y' :
    print("Apakah Anda Merasakan gejala berikut ini ? ")
    print("1. Perut Kembung")
    print("2. Mual")
    print("3. Nafsu Makan Menurun")
    print("4. Perut Terasa Sakit")
    ask1 = input("jawab (y/n) : ")

    

    if ask1 == 'y' :
        print("\nApakah anda juga merasakan gejala berikut ini ?")
        print("1. Naiknya Asam Lambung")
        print("2. Nyeri Ulu Hati")
        print("3. Sulit Bernafas")
        print("3. Pusing")
        ask2 = input("jawab (y/n) : ")
        
        
        if ask2 == 'y':
            print("\nHi, "+nama+" Hasil diagnosa kamu adalah : \n")
            print("Gejala Magh, Segera ke dokter")
        
            
            
        elif ask2 == 'n' :
            print("\nApakah Anda Juga Merasakan gejala berikut ini ? ")
            print("1. Nyeri Perut")
            print("2. Merasa Mual")
            print("3. Muntah")
            print("4. Kehilangan Nafsu Makan")
            ask3 = input("jawab (y/n) : ")
            
            
            
            if ask3 == 'y' :
                print("\nHi, "+nama+" Hasil diagnosa kamu adalah : ")
                print("Gejala Usus Buntu, Segera ke dokter")
                
                
            elif ask3 == 'n' :
                print("\nHi, "+nama+" Sepertinya anda sedang banyak fikiran\n")
            
            else :
                print("\nHi, "+nama+" Sepertinya anda tidak mau berobat")
                
    elif ask1 == 'n' :
        print("\nHi, "+nama+" Sepertinya anda butuh refreshing")
    
    else :
        print("\nHi, "+nama+" Sepertinya anda tidak mau berobat\n")
        
        print("+-----------------------------------------------+\n")
        
        os.system('clear')
    print("\n+-----------------------------------------------+")   
    pilihan = input("\nHallo "+nama+" , \nApakah anda ingin melakukan diagnosa ? (y/n) : ")
    
    if pilihan == 'y' :
        print("+-----------------------------------------------+")
        print("|\t\tSelamat Datang di Sistem Pakar\t\t\t|")
        print("|\t\tDeteksi Gejala Magh dan Usus Buntu\t\t|")
        print("+-----------------------------------------------+")
    os.system('clear')
    
else :
    print("\n")
    print("+-----------------Terima Kasih--------------+")
    print("+---------Selalu Jaga Kesehatan Anda--------+")