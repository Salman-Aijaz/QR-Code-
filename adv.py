import qrcode as qr
from PIL import Image

qr= qr.QRCode(
    version=1,
    error_correction=qr.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://www.linkedin.com/in/muhammad-salman-158213287/")

qr.make(fit=True)

img= qr.make_image(fill_color="black",back_color="white")

img.save("qr_code.png")