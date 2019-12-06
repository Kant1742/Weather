import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):
    app_id = '645748488394f0db0f3de32b6006ca70'
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=' + app_id
    cities = City.objects.all()
    all_cities = []

    #     form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()

    form = CityForm()

    for city in cities:
        resp = requests.get(url.format(city.name)).json()
        city_info = {
            'city': city.name,
            'temp': resp['main']['temp'],
            'icon': resp['weather'][0]['icon'],
            'descr': resp['weather'][0]['description']
        }
        all_cities.append(city_info)


    context = {'all_info': all_cities, 'form': form}

    return render(request, 'weather/index.html', context)
