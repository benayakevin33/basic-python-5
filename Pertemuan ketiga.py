# a = [1, 4, 5, 13]

# for x in a:
#     print("angkaku adalah " + x)

########################## RANGE ############################# 
# x = range (6)
# for i in x:
#     print(i)

# y = range(1, 9, 2)
# for i in y:
#     print (i)     

######################### PROGRAM FOR LOOP ############################# 

count = int(input("berapa banyak data: "))

#bikin list kosong
nama_pelanggan = []
umur_pelanggan = []

for i in range(count):
    print ("Data ke {}" .format (i+1))
    nama = input ("Nama: ")
    umur = int(input ("Umur: "))

    nama_pelanggan.append (nama)
    umur_pelanggan.append (umur)

for i in range(len(nama_pelanggan)):
    print("Pelanggan: {} dengan usia {}" .format (nama_pelanggan[i], umur_pelanggan[i] ))

########################## PROGRAM FOR  ############################# 

# for i in range(5):
#     if i == 3:
#         continue
#     print(i)

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

############ ############## PROGRAM WHILE ############################# 

# while True:
#     text = input("masukkan text: ")
#     if text == "stop" or text == "end":
#         break
#     print("text tersebut adalah: {}" .format(text))

