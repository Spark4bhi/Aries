import requests

def get_weather(city):
    url = f"https://www.google.com/search?q={city}+weather"
    res = requests.get(url)
    data = res.text
    start = data.find("<span class=\"wob_t\" id=\"wob_tm\"")
    end = data.find("</span>", start)
    temperature = data[start:end].split(">")[-1]
    start = data.find("<span id=\"wob_dc\" class=\"wob_dc\">")
    end = data.find("</span>", start)
    weather = data[start:end].split(">")[-1]
    return f"Currently in {city}, it is {temperature} degrees and {weather}."
