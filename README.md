# My Weather App

A simple Python CLI app that displays the current weather and local time for any city in the world.

## Features
- Search by city name
- Choose between Celsius and Fahrenheit
- Displays the latitude and longitude of the selected city
- Displays the current local time and timezone of the selected city
- No API key required

## Requirements
- Python 3
- No external dependencies (uses only stdlib)

## Usage
```bash
python3 weather.py
```
You will be prompted to:
1. Enter a city name (e.g. `London`)
2. Choose a temperature unit — `C` for Celsius, `F` for Fahrenheit

### Example output
```
Weather for Durban, South Africa
  Latitude    : -29.8579
  Longitude   : 31.0292
  Local time  : 2026-03-28 14:00 (Africa/Johannesburg)
  Temperature : 33.6°C
  Humidity    : 53%
```

## Data Source
Weather data is provided by [Open-Meteo](https://open-meteo.com/) — free and no API key needed.
