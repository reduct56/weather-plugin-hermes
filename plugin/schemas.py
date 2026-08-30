WEATHER_SCHEMA = {
    "name": "get_weather",
    "description": (
        "Get current weather for a city using the local weather backend. "
        "Use this tool when the user asks about current weather."
    ),
    "parameters": {
        "type": "object",
        "properties": {
            "city": {
                "type": "string",
                "description": "City name, for example Novosibirsk or Moscow"
            }
        },
        "required": ["city"]
    }
}