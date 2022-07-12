import json

import requests
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    """Render the html file."""

    return render(request, "index.html", {"MAP_KEY": settings.MAP_KEY})


def get_weather_data(request):
    """
    This will get the data from the url.
    """

    lat=request.GET.get('lat') or 51.5 
    lon=request.GET.get('lon') or -0.25
    url = "https://api.met.no/weatherapi/locationforecast/2.0/compact/"
    url += f"?lat={lat}&lon={lon}"

    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers=headers)
    if response.ok:
        res_json = response.json()
        data = {"success":True, "data":res_json["properties"]}
        return HttpResponse(content=json.dumps(data), status=200)
    return HttpResponse(content=json.dumps(success=False), status=400)
