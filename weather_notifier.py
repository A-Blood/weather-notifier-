DEBUG_MODE = True

# ========== Import Libraries ==========
import requests
import yagmail
import os
from dotenv import load_dotenv, find_dotenv
import schedule
import time
from datetime import datetime
# =======================================

# ========== Load Environment Variables ==========
dotenv_path = find_dotenv(filename="config.env")
load_dotenv(dotenv_path=dotenv_path)

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_PASSWORD")
API_KEY = os.getenv("WEATHER_API_KEY")
CITY = os.getenv("CITY")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER")

print(f"EMAIL: {EMAIL}")
print(f"CITY: {CITY}")
print(f"EMAIL_RECEIVER: {EMAIL_RECEIVER}")

required_vars = ["EMAIL_ADDRESS", "EMAIL_PASSWORD", "WEATHER_API_KEY", "EMAIL_RECEIVER", "CITY"]

for var in required_vars:
    if not os.getenv(var):
        raise Exception(f"Environment variable {var} is missing. Check your config.env file!")
# =================================================

# ========== Configuration and Settings ==========
def get_weather():
    url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if response.status_code != 200:
        raise Exception(f"Error fetching weather: {data.get('message')}")

    weather = data['weather'][0]['main']
    temp = data['main']['temp']
    return weather, temp

def send_email(subject, message):
    yag = yagmail.SMTP(EMAIL, PASSWORD)
    yag.send(to=EMAIL_RECEIVER, subject=subject, contents=message)

def main():
    try:
        now = datetime.now()
        current_time = now.strftime("%H:%M")

        if current_time == "06:00" or DEBUG_MODE:
            weather, temp = get_weather()
            print(f"Weather: {weather}, Temp: {temp}°C")

            if weather.lower() in ["rain", "drizzle", "thunderstorm"]:
                send_email(
                    subject="Weather Alert: Rain Incoming!",
                    message=f"Today’s weather is {weather} with {temp}°C. Check Buienalarm for more specific data. Don’t forget your umbrella!"
                )
                print("Rain alert email sent.")
            else:
                send_email(
                    subject="No rain!",
                    message=f"Today’s weather is {weather} with {temp}°C. No rain expected — have a great day!"
                )
                print("No rain email sent.")
        else:
            print(f"Not 6:00 AM yet. Current time: {current_time}. No email sent.")

    except Exception as e:
        print(f"Error: {e}")

# ========= Main Execution =========
if __name__ == "__main__":
    main()

    # Schedule the main function at 6:00 AM every day
    schedule.every().day.at("06:00").do(main)

    while True:
        schedule.run_pending()
        now = datetime.now().strftime("%H:%M:%S")
        print(f"[{now}] Waiting...")
        time.sleep(60)
