import qrcode as qr
img = qr.make("https://www.linkedin.com/in/muhammad-salman-158213287/")
img.save("my_linkedin.png")