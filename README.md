# My Weather App

A simple Python CLI app that displays the current temperature and humidity for any city in the world.

## Features
- Search by city name
- Choose between Celsius and Fahrenheit
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
  Temperature : 33.6°C
  Humidity    : 53%
```

## Data Source
Weather data is provided by [Open-Meteo](https://open-meteo.com/) — free and no API key needed.
