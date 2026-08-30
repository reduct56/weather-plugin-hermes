import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()
api = os.getenv("WEATHER_API_KEY")

app = FastAPI()

@app.get("/api/weather")
async def get_weather(city: str):
    # retrieve coodrinates via city using geocoding api
    lat, lon = await get_coordinates(city)

    # get json with general weather data via coordinates using openmeteo api
    data = await get_data(lat, lon)

    # retrieve weather data via coordinates using openmeteo api
    temperature = get_temperature(data)
    humidity = get_humidity(data)
    wind_state = get_wind_state(data)

    return {
        "city": city,
        "temperature": temperature,
        "humidity": humidity,
        "wind_state": wind_state
    }

async def get_data(lat, lon) :
    data = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,wind_direction_10m")
    return data.json()

async def get_coordinates(city: str):
    data = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api}").json()
    lat = data[0].get('lat')
    lon = data[0].get('lon')
    return lat, lon

def get_temperature(data):
    return str(data.get("current").get("temperature_2m")) + data.get("current_units").get("temperature_2m")

def get_humidity(data):
    return str(data.get("current").get("relative_humidity_2m")) + data.get("current_units").get("relative_humidity_2m")

def get_wind_state(data):
    return get_wind_speed(data) + " " + get_wind_direction_text(data.get("current").get("wind_direction_10m"))

def get_wind_speed(data: dict):
    return str(data.get("current").get("wind_speed_10m")) + data.get("current_units").get("wind_speed_10m")

def get_wind_direction_text(degrees: float) -> str:
    directions = ["North", "Northeast", "East", "Southeast",
                  "South", "Southwest", "West", "Northwest"]
    idx = int((degrees + 22.5) % 360 // 45)
    return directions[idx]
