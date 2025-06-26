import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import sys

# Constants
API_KEY = '85643ea318e7455ac3025d6bdd6eb14f'  # Replace with your actual API key
CITY = 'London'
UNITS = 'metric'  # or 'imperial'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&units={UNITS}&appid={API_KEY}'

def fetch_weather_data():
    response = requests.get(URL)
    if response.status_code != 200:
        print("Error fetching data:", response.status_code)
        sys.exit(1)
    return response.json()

def parse_forecast_data(data):
    forecast_list = data['list']
    times, temps, humidities = [], [], []

    for entry in forecast_list:
        dt = datetime.fromtimestamp(entry['dt'])
        temp = entry['main']['temp']
        humidity = entry['main']['humidity']
        times.append(dt)
        temps.append(temp)
        humidities.append(humidity)
        

    return times, temps, humidities
def plot_dashboard(times, temps, humidities):
    sns.set(style='darkgrid')

    plt.figure(figsize=(14, 6))

    # Temperature Plot
    plt.subplot(1, 2, 1)
    sns.lineplot(x=times, y=temps, marker='o', color='tomato')
    plt.title('Temperature Forecast')
    plt.xlabel('DateTime')
    plt.ylabel('Temperature (°C)')
    plt.xticks(rotation=45)

    # Humidity Plot
    plt.subplot(1, 2, 2)
    sns.lineplot(x=times, y=humidities, marker='o', color='skyblue')
    plt.title('Humidity Forecast')
    plt.xlabel('DateTime')
    plt.ylabel('Humidity (%)')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()
if __name__ == '__main__':
    data = fetch_weather_data()
    times, temps, humidities = parse_forecast_data(data)
    plot_dashboard(times, temps, humidities)

