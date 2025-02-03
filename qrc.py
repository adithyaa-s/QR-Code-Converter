import qrcode

def generate_qr(url, filename="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(filename)
    print(f"QR Code saved as {filename}")

# Enter URL Here
url = ""
generate_qr(url)
