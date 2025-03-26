import os

import requests
from apscheduler.schedulers.blocking import BlockingScheduler
import psycopg2
from datetime import datetime
import dotenv

API_KEY = os.getenv("API_KEY")
URL = os.getenv("URL")
CITY = os.getenv("CITY")

DB_PARAMS = {
    "dbname": "weather",
    "user": "postgres",
    "password": "password",
    "host": "localhost",
    "port": "5432",
}
def fetch_weather():
    response = requests.get(URL)
    data = response.json()

    temp = data['main']['temp'] - 273.15
    humidity = data['main']['humidity']
    timestamp = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    conn = psycopg2.connect(**DB_PARAMS)
    cur = conn.cursor()
    cur.execute(cur.execute("""
        INSERT INTO weather (city, temperature, humidity, timestamp)
        VALUES (%s, %s, %s, %s)
    """, (CITY, temp, humidity, timestamp)))
    conn.commit()
    cur.close()
    conn.close()

schedule = BlockingScheduler()
schedule.add_job(fetch_weather, 'interval', minutes=20)
schedule.start()

if __name__ == '__main__':
    fetch_weather()