import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheets authentication
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

# Open the Google Sheet
sheet = client.open("AttendanceSheet").sheet1  # Change to your sheet name

def update_attendance(qr_data):
    try:
        sheet.append_row([qr_data])  # Append scanned data to a new row
        return True
    except Exception as e:
        print(f"Error updating sheet: {e}")
        return False
