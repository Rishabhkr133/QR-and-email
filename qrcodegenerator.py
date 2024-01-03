import qrcode

features = qrcode.QRCode(version=1,box_size=10,border=2)
features.add_data('https://www.bing.com/images/search?q=Instagram+Logo+Flat&FORM=RESTAB')

features.make(fit=True)
genrate_image = features.make_image (fill_color="black",back_cokor="white")

genrate_image.save("qrcode3.png")