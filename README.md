# inverter2
# EG4 Battery Monitor Web App

This is a minimal Flask application that displays battery voltage from an EG4 inverter using the [eg4-inverter-api](https://pypi.org/project/eg4-inverter-api/) library.

## Setup

```bash
pip install -r requirements.txt
python web/app.py
```

Make sure you are running Python 3.8 or higher. The application starts a local
Flask server on port 8000.

Then open `http://localhost:8000` in your browser. An activity log at the bottom explains every action the server performs. It starts with a startup message, shows each API request with timing information and any returned errors, and updates a countdown timer to the next voltage check. After a successful login your credentials are stored locally and battery voltage is retrieved every 30 seconds for display on a line chart (if Chart.js is available).

If you encounter indentation errors, ensure your editor uses spaces not tabs.
