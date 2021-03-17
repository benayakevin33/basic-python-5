a = input ("Masukkan nilai ujian teori Anda : ")
b = input ("Masukkan nilai ujian praktik Anda : ")

teori = float (a)
praktik = float (b)

if (teori >= 70 and praktik >=70):
    print ("Selamat, anda lulus!")

elif (teori >= 70 and praktik < 70):
    print ("Anda harus mengulang ujian praktik.")

elif (teori < 70 and praktik >= 70):
    print ("Anda harus mengulang ujian teori.")

elif (teori < 70 and praktik < 70):
    print ("Anda harus mengulang ujian teori dan praktik.")

else:
    print ("Error")