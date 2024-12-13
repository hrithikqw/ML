import qrcode

def generate_qr_code(data):
    # Create QR code
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Size of each box in the QR code
        border=4,  # Thickness of the border
    )
    
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code
    img = qr.make_image(fill='black', back_color='white')
    img.show()  # Show the QR code image
    img.save('url_qrcode.png')  # Save the QR code to a file

# Example usage
data = "https://www.youtube.com"
generate_qr_code(data)
