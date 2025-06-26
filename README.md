# API-INTEGRATION-AND-DATA-VISUALIZATION
COMPANY: CODTECH IT SOLUTIONS
NAME:  C Kishore
INTERN ID: CT06DN863
DOMAIN: Python Programming
DURATION: 6 weeks
MENTOR: NEELA SANTOSH

📄 Weather Forecast Dashboard using OpenWeatherMap API
This project demonstrates how to build a Python-based weather forecast dashboard using real-time weather data from the OpenWeatherMap API. The script fetches forecast data for a specified city (default is London), processes the data to extract relevant features like temperature and humidity, and generates visual charts to display the trends over time. It is a great example of combining APIs, data handling, and visualization in a Python automation task.

🔧 Technologies and Libraries Used:
requests – To fetch data from the OpenWeatherMap API

datetime – For handling and formatting timestamps

matplotlib and seaborn – For plotting temperature and humidity graphs

sys – To gracefully handle API errors

🔍 How the Project Works:
Step 1: Setup API and Configuration
At the beginning of the script, you define constants such as your API key, the city name, and units (metric for Celsius or imperial for Fahrenheit). The URL is dynamically generated using these constants.

Step 2: Fetch Weather Data
The fetch_weather_data() function sends an HTTP GET request to the OpenWeatherMap forecast API. If the request fails (e.g., invalid API key or wrong city name), the program exits with an error message. On success, it returns a JSON object containing weather forecast data for the next five days at 3-hour intervals.

Step 3: Parse Forecast Data
The parse_forecast_data() function processes the JSON response. It extracts:

The timestamp (dt)

The temperature (temp)

The humidity (humidity)

Each timestamp is converted from UNIX format into a readable date-time using Python’s datetime.fromtimestamp(). These values are stored in separate lists for plotting.

Step 4: Plot the Dashboard
The plot_dashboard() function uses seaborn and matplotlib to generate two side-by-side line plots:

A temperature forecast graph showing how the temperature changes over time.

A humidity forecast graph showing the percentage of humidity during the same intervals.

These graphs are styled using Seaborn’s dark grid theme and are fully labeled for clarity, including rotated X-axis timestamps for better readability.

Step 5: Run the Program
When the script is run directly (__name__ == '__main__'), it:

Fetches the weather data,

Parses the required fields,

Displays the dashboard with temperature and humidity graphs.

📌 How to Use:
Replace the API_KEY with your own key from https://openweathermap.org/api.

(Optional) Change the CITY value to any city of your choice.

Run the script using Python 3.

✅ Conclusion:
This weather forecast dashboard project effectively integrates real-time data from an external API with powerful visualization tools in Python. It can be extended further to include wind speed, pressure, or even alerts, making it a great starting point for weather-based applications or dashboards.

![Image](https://github.com/user-attachments/assets/d51acad9-d6dc-4f2c-9791-1bcb061e6b7d)
