phi = 22/7

jari = input("Masukkan nilai jari-jari lingkaran : ")
r = float (jari)

luas = phi * (r ** 2)

text1 = "Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2." .format (jari, luas)
print (text1)

text2 = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2." .format (jari, luas)
print (text2)