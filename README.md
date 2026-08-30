# Hermes agent Weather plugin
___
This plugin allows you to get weather data in city that hermes gets from user request.
___
## Installation steps
**Hermes**:
1. Make sure you have hermes agent installed
2. Create a directory "weather-api" in hermes/plugins folder (root directory of hermes)
3. Move 4 files from plugin/ folder to "weather-api" directory you created previously
4. Open shell/bash and type ```hermes plugins enable weather-api```

**Backend**:
1. Locate into backend folder
2. Install the requirements.txt
3. Create `.env` file and write there `WEATHER_API_KEY` OpenWeatherMap API
4. Run ```fastapi run main.py```

#### Then you can run `hermes` and use it. Just ask agent about weather somewhere and it will respond with weather data