import requests

def fetch_weather_data(url):
    response = requests.get(url)
    data = response.text
    lines = data.split('\n')
    headers = lines[6].split()  # Assuming the 7th line contains headers
    weather_data = []

    for line in lines[7:]:
        if line.strip():
            parts = line.split()
            year_data = dict(zip(headers, parts))
            weather_data.append(year_data)

    return weather_data
