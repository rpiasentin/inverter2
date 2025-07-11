#!/usr/bin/env python3
"""EG4 battery monitor Flask app.

This backend exposes endpoints to log in to the EG4 cloud API and fetch the
battery voltage. A small in-memory log is also kept to help debug API calls.
"""


import os
from flask import Flask, request, jsonify, send_from_directory
main
import asyncio
import logging
import os
from datetime import datetime

from eg4_inverter_api.client import EG4InverterAPI
from flask import Flask, jsonify, request, send_from_directory

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

api_client = None
serial_number = None
log_messages = []

# Initial log entry so the user sees immediate feedback
def _init_log():
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - Server started. Awaiting login credentials."
    log_messages.append(entry)
    logging.info(entry)

_init_log()


# Initial log entry so the user sees immediate feedback
def _init_log():
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - Server started. Awaiting login credentials."
    log_messages.append(entry)
    logging.info(entry)


_init_log()


# Initial log entry so the user sees immediate feedback
def _init_log():
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - Server started. Awaiting login credentials."
    log_messages.append(entry)
    logging.info(entry)


_init_log()


# Initial log entry so the user sees immediate feedback
def _init_log():
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - Server started. Awaiting login credentials."
    log_messages.append(entry)
    logging.info(entry)


_init_log()


# Initial log entry so the user sees immediate feedback
def _init_log():
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - Server started. Awaiting login credentials."
    log_messages.append(entry)
    logging.info(entry)


_init_log()


def add_log(message: str) -> None:
    """Store a timestamped log message for troubleshooting."""
    timestamp = datetime.now().strftime("%H:%M:%S")
    entry = f"{timestamp} - {message}"
    log_messages.append(entry)
    if len(log_messages) > 100:
        log_messages.pop(0)
    app.logger.info(entry)


@app.route("/")
def index():
    # Serve the frontend HTML regardless of working directory
    frontend_dir = os.path.dirname(os.path.abspath(__file__))
    return send_from_directory(frontend_dir, "index.html")


@app.route("/api/logs")
def logs():
    """Return recent API interaction logs."""
    return jsonify({"log": log_messages})


@app.route("/api/login", methods=["POST"])
def login():
    global api_client, serial_number
    data = request.get_json()
    if not data or "username" not in data or "password" not in data:
        return jsonify({"success": False, "error": "Missing credentials"}), 400

    username = data["username"]
    password = data["password"]

    api_client = EG4InverterAPI(username, password)





    add_log("Attempting to log in to the EG4 cloud")
main


    try:
        add_log("Sending login request...")
        asyncio.run(api_client.login())
        add_log("Login request complete. Processing response")
        inverters = api_client.get_inverters()
        if not inverters:



            add_log("Login succeeded but no inverters were found for this account")
            return jsonify({"success": False, "error": "No inverters found"}), 400
main


        serial_number = inverters[0].serialNum
        api_client.set_selected_inverter(inverterIndex=0)
        add_log(
            f"Login successful. Selected inverter {serial_number}. Starting periodic voltage checks."
        )
        return jsonify({"success": True, "serial": serial_number})
    except Exception as e:
        api_client = None
        add_log(f"Login failed with error: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


@app.route("/api/voltage")
def voltage():
    if not api_client or not serial_number:
        add_log("Voltage requested without login")
        return jsonify({"success": False, "error": "Not logged in"}), 400
    try:





        add_log("Requesting current battery voltage from inverter")
main



        battery_data = api_client.get_inverter_battery()
        # Use totalVoltageText from overall data
        voltage = float(battery_data.totalVoltageText)
        add_log(f"Received voltage reading: {voltage} V")
        return jsonify({"success": True, "voltage": voltage})
    except Exception as e:
        add_log(f"Error retrieving voltage: {e}")
        return jsonify({"success": False, "error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
