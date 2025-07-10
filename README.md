# EG4 Battery Monitor Web App

This is a minimal Flask application that displays battery voltage from an EG4 inverter using the [eg4-inverter-api](https://pypi.org/project/eg4-inverter-api/) library.

## Setup

```bash
pip install -r requirements.txt
python web/app.py
```

Make sure you are running Python 3.8 or higher. The application starts a local
Flask server on port 8000.

Then open `http://localhost:8000` in your browser. The page includes a log window below the login form showing API activity. After a successful login your credentials are stored in local storage and battery voltage is retrieved every 30 seconds for display on a line chart.
