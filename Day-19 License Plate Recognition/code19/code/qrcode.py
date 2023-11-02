import qrcode
from PIL import Image
data ="https://igetintopc.com/mysql-community-server-8-0-21-free-download/"
qr= qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(data)
qr.make(fit=True)
image=qr.make_image(fill="black", back_color="white")
image.save("qr_code.png")
Image.open("qr_code.png")