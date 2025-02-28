from flask import Flask, request, jsonify, render_template
import cv2

import google_sheets

app = Flask(__name__)

# Route to render HTML page
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint to scan QR and update attendance
@app.route('/scan', methods=['POST'])
def scan_qr():
    qr_data = request.json.get('qr_data')
    
    if not qr_data:
        return jsonify({"error": "No QR data received"}), 400
    
    # Update Google Sheets
    success = google_sheets.update_attendance(qr_data)
    
    if success:
        return jsonify({"message": "Attendance updated successfully!"})
    else:
        return jsonify({"error": "Failed to update attendance"}), 500

if __name__ == '__main__':
    app.run(debug=True)
