import urllib.request
import json

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

    # Step 2: Fetch weather
    temp_unit = "fahrenheit" if use_fahrenheit else "celsius"
    wx_url = (f"https://api.open-meteo.com/v1/forecast"
              f"?latitude={lat}&longitude={lon}"
              f"&current=temperature_2m,relative_humidity_2m"
              f"&temperature_unit={temp_unit}")
    with urllib.request.urlopen(wx_url) as r:
        wx = json.loads(r.read())
    current = wx["current"]
    temp = current["temperature_2m"]
    humidity = current["relative_humidity_2m"]
    units = wx["current_units"]

    print(f"\nWeather for {name}, {country}")
    print(f"  Temperature : {temp}{units['temperature_2m']}")
    print(f"  Humidity    : {humidity}{units['relative_humidity_2m']}")

if __name__ == "__main__":
    city = input("Enter city name: ").strip()
    unit_choice = input("Temperature unit - (C)elsius or (F)ahrenheit? [C]: ").strip().upper()
    use_fahrenheit = unit_choice == "F"
    if city:
        get_weather(city, use_fahrenheit)
