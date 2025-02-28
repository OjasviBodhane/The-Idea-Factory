from flask import Flask, render_template, send_file
import qrcode

app = Flask(__name__)

@app.route('/')
def generate_qr():
    data = "CS101_280224"  # Lecture ID
    qr = qrcode.make(data)
    qr.save("attendance_qr.png")
    return send_file("attendance_qr.png", mimetype="image/png")

if __name__ == '__main__':
    app.run(debug=True)
