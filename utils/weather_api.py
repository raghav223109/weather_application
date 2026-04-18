import requests
import os
import time
import logging
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

# 📜 Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# 🔁 Retry mechanism
def fetch_with_retry(url, retries=3):
    for i in range(retries):
        try:
            response = requests.get(url, timeout=5)
            return response.json()
        except Exception as e:
            logging.error(f"Retry {i+1} failed: {e}")
            time.sleep(1)
    return None


def get_current_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
        data = fetch_with_retry(url)

        if not data or data.get("cod") != 200:
            return None

        return {
            "temp": int(data['main']['temp'] - 273.15),
            "humidity": data['main']['humidity'],
            "pressure": data['main']['pressure'],
            "wind": data['wind']['speed'],
            "condition": data['weather'][0]['main'],
            "description": data['weather'][0]['description'],
            "icon": data['weather'][0]['icon'],
            "lat": data['coord']['lat'],
            "lon": data['coord']['lon']
        }

    except Exception as e:
        logging.error(f"Current weather error: {e}")
        return None


def get_forecast(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}"
        data = fetch_with_retry(url)

        if not data or data.get("cod") != "200":
            return None, None

        temps, times = [], []

        for item in data['list']:
            temps.append(int(item['main']['temp'] - 273.15))
            times.append(item['dt_txt'])

        return times, temps

    except Exception as e:
        logging.error(f"Forecast error: {e}")
        return None, None