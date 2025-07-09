from flask import Flask, request, jsonify, send_from_directory
import asyncio
from eg4_inverter_api.client import EG4InverterAPI

app = Flask(__name__)

api_client = None
serial_number = None

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/login', methods=['POST'])
def login():
    global api_client, serial_number
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'success': False, 'error': 'Missing credentials'}), 400

    username = data['username']
    password = data['password']

    api_client = EG4InverterAPI(username, password)
    try:
        asyncio.run(api_client.login())
        inverters = api_client.get_inverters()
        if not inverters:
            return jsonify({'success': False, 'error': 'No inverters found'}), 400
        serial_number = inverters[0].serialNum
        api_client.set_selected_inverter(inverterIndex=0)
        return jsonify({'success': True, 'serial': serial_number})
    except Exception as e:
        api_client = None
        return jsonify({'success': False, 'error': str(e)}), 500

@app.route('/api/voltage')
def voltage():
    if not api_client or not serial_number:
        return jsonify({'success': False, 'error': 'Not logged in'}), 400
    try:
        battery_data = api_client.get_inverter_battery()
        # Use totalVoltageText from overall data
        voltage = float(battery_data.totalVoltageText)
        return jsonify({'success': True, 'voltage': voltage})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

