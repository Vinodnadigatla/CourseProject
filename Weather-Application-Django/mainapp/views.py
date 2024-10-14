from django.shortcuts import render
import requests  # For sending requests

# Create your views here.

def index(request):
    # Using Weather API
    BASE_URL = 'http://api.weatherapi.com/v1'
    API_KEY = 'f80f6e21edd74a4f946112307240910'  # Your API Key

    if request.method == 'POST':
        city = request.POST.get('city').lower()
        print(city)

        # Check if city input is empty
        if city == '':
            print('No value')
            return render(request, 'index.html', {'checker': 'Please enter valid info...!'})

        # Prepare request URL
        request_url = f"{BASE_URL}/current.json?key={API_KEY}&q={city}&aqi=no"

        # Make a GET request to the Weather API
        response = requests.get(request_url)

        if response.status_code == 200:
            data = response.json()
            location = data['location']
            weather = data['current']

            # Prepare context for rendering
            context = {
                'weather': weather['temp_c'],
                'city_name': location['name'],
                'region': location['region'],
                'country': location['country'],
                'lat': location['lat'],
                'lon': location['lon'],
                'localtime': location['localtime'],
                'continent': location['tz_id'],
                'static_city': city
            }

            return render(request, 'index.html', context)
        else:
            print("An error occurred:", response.status_code)
            return render(request, 'index.html', {'static_city': city, 'checker': 'Please enter a valid city'})

    return render(request, 'index.html', {})
