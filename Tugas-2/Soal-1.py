print ("Selamat Datang!")
count = 0 #untuk menyatakan data ke-

#bikin list kosong
nama = []
telepon = []

while True:
    print ("--- Menu ---")
    print ("1. Daftar Kontak")
    print ("2. Tambah Kontak")
    print ("3. Keluar")
    print ("")

    user = input("Pilih menu: ")
    print ("")

    #Pilihan menu pertama
    if user == "1":
        print("Daftar kontak:")

        for a in range (count):
            print ("Nama: " + nama[a])
            print ("No Telepon: " + telepon[a])
            print ("")

    #Pilihan menu kedua
    elif user == "2":
        name = input ("Nama: ")
        phone = input ("No Telepon: ")
        print ("")

        nama.append (name)
        telepon.append (phone)

        count = count + 1
    
    #Pilihan menu ketiga
    elif user == "3":
        print ("Program selesai, sampai jumpa!")
        break

    #pilihan error
    else:
        print ("Menu tidak tersedia")
        print ("")