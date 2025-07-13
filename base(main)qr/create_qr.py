import segno
import os
os.makedirs('qrcode',exist_ok=True) #создание файла
d=0
with open('base(main)qr/prev.txt','r') as p: 
    tir=p.readlines()   #считываем файл
    for link in tir:
        d+=1
        qr=segno.make_qr(link.strip())
        qr.save(f'qrcode/{d}.png',scale=15,border=2) # добавление qr в отдельный файл 'qrcode'
