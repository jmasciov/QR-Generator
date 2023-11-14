## Import library
import qrcode

img = qrcode.make('https://www.espn.com/')
type(img)
img.save("some_file.png")




import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://www.espn.com/')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("test_qr.png")