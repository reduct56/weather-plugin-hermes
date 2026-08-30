import json
import requests
import fastapi

FASTPI_URL = "http://127.0.0.1:8000"

def get_weather(city: str) -> str:
    try:
        response = requests.get(f"{FASTPI_URL}/api/weather", params={'city': city})
        response.raise_for_status()
        return json.dumps(response.json(), ensure_ascii=False)
    except requests.RequestException as e:
        return json.dumps({"error": "Weather backend is unavailable"}, ensure_ascii=False)
    except Exception as e:
        return json.dumps({"error": str(e)}, ensure_ascii=False)
