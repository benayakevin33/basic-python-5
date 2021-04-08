import smtplib
from email.mime.text import MIMEText #terdiri atas subject, isi email, dan alamat pengirim dan penerima
from email.mime.multipart import MIMEMultipart 
from email.mime.base import MIMEBase
from email import encoders
import os.path

jumlah_penerima = int(input ("Berapa email yang ingin anda kirim : "))

a = 0
#untuk memasukkan banyaknya email yang ingin dituju
while a < jumlah_penerima:
    recevier = input ("Masukkan email yang ingin dituju: ")
    a = a + 1

    penerima = open ("receiver_list.txt", "a")
    penerima.write (recevier + ",")
    penerima.close()

email_user = "benayakevin33@gmail.com" #email pengirim
password_user = "b3n4y@12345" #password email pengirim

subject = "Hello Benaya Kevin" #subject dalam email
body = "Hello Ben, nice to meet you" #isi pesan dalam email

msg = MIMEMultipart ()
msg ['From']= email_user #untuk pengirim
msg ['Subject'] = subject #untuk subject

file_penerima = open ("receiver_list.txt", "r") #membuka semua email yang telah ditulis ke dalam file
email_send = str(file_penerima.read()) #membuat semua tulisan dalam bentuk string
file_penerima.close()

msg ['To']  = email_send
    
msg.attach (MIMEText (body, "plain"))

#Untuk menambah lampiran
file_location = "C:\\Users\\Ben\\basic-python-5\\Final-Project\\Document.txt"
#file_location = 'E:\\Foto\\Me\\ben.jpg'

filename = os.path.basename (file_location) #untuk mengambil ekor (dokumen.txt)
attachment = open (file_location, "rb") #membaca dalam mode binary

part = MIMEBase ('application', 'octet-stream') #untuk jenis file yang tidak diketahui
part.set_payload (attachment. read())
encoders.encode_base64 (part) #untuk mengamankan isi dari file yang kita kirim, jadi tidak bisa dilihat orang
part.add_header ('Content-Disposition', 'attachment; filename = %s' % filename)

# Melampirkan lampiran ke dalam MIMEmultipart object
msg.attach(part)

text = msg.as_string () #membuat pesan yang dikirim menjadi dalam bentuk string

server = smtplib.SMTP_SSL("smtp.gmail.com", 465) #untuk masuk server (nama dan port nya)
server.login (email_user, password_user) #login ke email

server.sendmail(email_user, email_send.split(","), text) #untuk mengirimkan email
server.quit() #untuk keluar (disconect) dari server

print("Email telah terkirim, silahkan cek email anda. Terima kasih") #pesan akhir

#untuk menghapus semua isi di dalam file receiver_list.txt
import os
os.remove ("receiver_list.txt")