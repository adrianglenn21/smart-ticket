import requests
import json
import datetime

def get_current_weather() -> json:
    city = 'Manila'
    api_key = '5fd2f8004c072495fe5a282a6ad6b66e'

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    result = {
    }

    if response.status_code == 200:
        # The request was successful!
        data = response.json()
        # print(json.dumps(data, indent=4))
        result['city'] = data['name']
        result['temp'] = data['main']['temp']
        result['country'] = get_country_name(data['sys']['country'])
        result['feels_like'] = data['main']['feels_like']
        result['timestmp'] = datetime.datetime.now().strftime("%A, %d %B %Y")
        result['temp_min'] = data['main']['temp_min']
        result['temp_max'] = data['main']['temp_max']

    else:
        # There was an error with the request.
        print("Error:", response.status_code)

    return result


def get_country_name(short_name: str) -> str:
    values = {
        "US": "United States",
        "GB": "United Kingdom",
        "CA": "Canada",
        "AU": "Australia",
        "FR": "France",
        "DE": "Germany",
        "JP": "Japan",
        "CN": "China",
        "IN": "India",
        "BR": "Brazil",
        "PH": "Philippines"
    }

    return values[short_name]

    