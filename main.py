import qrcode
from js import document
import base64
from io import BytesIO

def generate_qr(*args, **kwargs):
    text = document.getElementById("qrinput").value
    if not text:
        document.getElementById("output").innerHTML = "❗ Please enter text"
        retur
    # Generate QR code image
    img = qrcode.make(text)
    # Save image to buffer
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    buffer.seek(0)
    # Encode image as base64
    img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode('ascii')
    # Display image in browser
    document.getElementById("output").innerHTML = f'<img src="data:image/png;base64,{img_base64}" />'