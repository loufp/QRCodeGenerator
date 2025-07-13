import segno
import os
os.makedirs('qrcode',exist_ok=True)
while True:
    w=input()
    with open('/Users/kirillkirill13let/Desktop/qr(none_stop)/base(main)qr/prev.txt','w') as r:
        r.write(w)
        d=0
        with open('base(main)qr/prev.txt','r') as p: 
            tir=p.readlines()
            for link in tir:
                d+=1
                qr=segno.make_qr(link.strip())
                qr.save(f'qrcode/{d}.png',scale=15,border=2)
    if w=='1':break