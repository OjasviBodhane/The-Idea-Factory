import qrcode

def generate_qr(lecture_id):
    """Generate and save QR Code for the lecture."""
    qr = qrcode.make(lecture_id)
    qr.save(f"{lecture_id}.png")
    print(f"QR Code saved as {lecture_id}.png")

# Example usage:
generate_qr("CS101_280224")  # Lecture ID = Course Code + Date
