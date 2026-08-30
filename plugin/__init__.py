from .schemas import WEATHER_SCHEMA
from .tools import get_weather

def register(ctx):
    ctx.register_tool(
        name="get_weather",
        toolset="weather_api",
        schema=WEATHER_SCHEMA,
        handler=lambda args, **kwargs: get_weather(
            args.get("city", "")
        ),
        description="Get current weather for a city"
    )