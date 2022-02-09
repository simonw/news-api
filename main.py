import os
from newsapi import NewsApiClient
from time import strftime
from json import dumps

COUNTRIES_LANGUAGES = {"in": "en", "us": "en", "gb": "en"}
CATEGORIES = ["business","health","entertainment", "general", "science", "sports", "technology"]


def update_top_headline():
    FIRSTAPI = os.environ.get("FIRSTAPI")
    SECONDAPI = os.environ.get("SECONDAPI")
    # for loop to iterate through the categories and country
    for category in CATEGORIES:
        for country in COUNTRIES_LANGUAGES:
            print(f"Started category:{category} country:{country} at {strftime('%X %d %B %Y')}")
            try:
                newsapi = NewsApiClient(api_key=FIRSTAPI)
                top_headlines = newsapi.get_top_headlines(category=category, country=country, language=COUNTRIES_LANGUAGES[country], page_size=100)
            except Exception as e:
                newsapi = NewsApiClient(api_key=SECONDAPI)
                top_headlines = newsapi.get_top_headlines(category=category, country=country, language=COUNTRIES_LANGUAGES[country], page_size=100)
            json_string = dumps(top_headlines)
            try:
                with open(f"{country}/{category}.json", "w") as outfile:
                    outfile.write(json_string)
            except Exception as e: 
                os.system(f"mkdir {country}")
                with open(f"{country}/{category}.json", "w") as outfile:
                    outfile.write(json_string)

update_top_headline()
