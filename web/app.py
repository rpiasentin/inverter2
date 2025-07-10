from flask import Flask, request, jsonify, send_from_directory
import asyncio
 325wbg-codex/build-web-app-to-read-battery-voltage
from datetime import datetime
import logging
=======
 main
from eg4_inverter_api.client import EG4InverterAPI

app = Flask(__name__)

 325wbg-codex/build-web-app-to-read-battery-voltage
logging.basicConfig(level=logging.INFO)

api_client = None
serial_number = None
log_messages = []

def add_log(message: str) -> None:
    """Store a timestamped log message for troubleshooting."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - {message}"
    log_messages.append(entry)
    if len(log_messages) > 100:
        log_messages.pop(0)
    app.logger.info(entry)
=======
api_client = None
serial_number = None
 main

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

 325wbg-codex/build-web-app-to-read-battery-voltage

@app.route('/api/logs')
def logs():
    """Return recent API interaction logs."""
    return jsonify({'log': log_messages})

=======
 main
@app.route('/api/login', methods=['POST'])
def login():
    global api_client, serial_number
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'success': False, 'error': 'Missing credentials'}), 400

    username = data['username']
    password = data['password']

    api_client = EG4InverterAPI(username, password)
 325wbg-codex/build-web-app-to-read-battery-voltage
    add_log("Attempting login")
=======
 main
    try:
        asyncio.run(api_client.login())
        inverters = api_client.get_inverters()
        if not inverters:
 325wbg-codex/build-web-app-to-read-battery-voltage
            add_log("No inverters found after login")
            return jsonify({'success': False, 'error': 'No inverters found'}), 400
        serial_number = inverters[0].serialNum
        api_client.set_selected_inverter(inverterIndex=0)
        add_log(f"Login successful. Selected inverter {serial_number}")
        return jsonify({'success': True, 'serial': serial_number})
    except Exception as e:
        api_client = None
        add_log(f"Login error: {e}")
=======
            return jsonify({'success': False, 'error': 'No inverters found'}), 400
        serial_number = inverters[0].serialNum
        api_client.set_selected_inverter(inverterIndex=0)
        return jsonify({'success': True, 'serial': serial_number})
    except Exception as e:
        api_client = None
 main
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/voltage')
def voltage():
    if not api_client or not serial_number:
 325wbg-codex/build-web-app-to-read-battery-voltage
        add_log("Voltage requested without login")
        return jsonify({'success': False, 'error': 'Not logged in'}), 400
    try:
        add_log("Requesting battery voltage")
        battery_data = api_client.get_inverter_battery()
        # Use totalVoltageText from overall data
        voltage = float(battery_data.totalVoltageText)
        add_log(f"Voltage response: {voltage}")
        return jsonify({'success': True, 'voltage': voltage})
    except Exception as e:
        add_log(f"Voltage error: {e}")
=======
        return jsonify({'success': False, 'error': 'Not logged in'}), 400
    try:
        battery_data = api_client.get_inverter_battery()
        # Use totalVoltageText from overall data
        voltage = float(battery_data.totalVoltageText)
        return jsonify({'success': True, 'voltage': voltage})
    except Exception as e:
 main
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

