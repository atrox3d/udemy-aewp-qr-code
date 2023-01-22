import qrcode

img = qrcode.make('hello, testing testing')
img.save('qr1.png')

