import urllib.request
import json
from datetime import datetime, timezone, timedelta

def get_weather(city, use_fahrenheit=False):
    # Step 1: Geocode
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"
    with urllib.request.urlopen(geo_url) as r:
        geo = json.loads(r.read())
    if not geo.get("results"):
        print(f"City '{city}' not found.")
        return
    result = geo["results"][0]
    lat, lon, name, country = result["latitude"], result["longitude"], result["name"], result["country"]
    timezone_str = result.get("timezone")

    # Step 2: Fetch weather (include UTC offset seconds for local time)
    temp_unit = "fahrenheit" if use_fahrenheit else "celsius"
    wx_url = (f"https://api.open-meteo.com/v1/forecast"
              f"?latitude={lat}&longitude={lon}"
              f"&current=temperature_2m,relative_humidity_2m"
              f"&temperature_unit={temp_unit}"
              f"&timeformat=unixtime&timezone={timezone_str}")
    with urllib.request.urlopen(wx_url) as r:
        wx = json.loads(r.read())
    current = wx["current"]
    temp = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    units = wx["current_units"]

    # Derive local time from the UTC offset provided in the response
    utc_offset_seconds = wx.get("utc_offset_seconds", 0)
    local_tz = timezone(timedelta(seconds=utc_offset_seconds))
    local_time = datetime.fromtimestamp(current["time"], tz=local_tz)

    print(f"\nWeather for {name}, {country}")
    print(f"  Local time  : {local_time.strftime('%Y-%m-%d %H:%M')} ({timezone_str})")
    print(f"  Temperature : {temp}{units['temperature_2m']}")
    print(f"  Humidity    : {humidity}{units['relative_humidity_2m']}")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    unit_choice = input("Temperature unit - (C)elsius or (F)ahrenheit? [C]: ").strip().upper()
    use_fahrenheit = unit_choice == "F"
    if city:
        get_weather(city, use_fahrenheit)
