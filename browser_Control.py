
import webbrowser
import wikipedia
from Mic_setup import say
import requests

def Search_Wiki(query):
    query=query.replace("wikipedia","")
    query=query.replace("search","")
    query=query.replace("vihaan","")
    result=wikipedia.summary(query,sentences=3)
    return result

def get_map(query):
    link=f"https://www.google.com/maps/search/{query}"
    webbrowser.open(link)
    say("opening google map")
    
def google_search(query):
    query=query.replace("search","")
    query=query.replace("google","")
    query=query.replace("on","")
    query=query.replace("tell me","")
    link=f"https://www.google.com/search?q={query} "
    webbrowser.open(link)
    say("searching on google")

def site_Call(query):
    sites=[["facebook","https://facebook.com"],["instagram","https://instagram.com"],["chat","https://chat.openai.com/"],["speedtest","https://www.speedtest.net/"]]
    for site in sites:
        if f"open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} as per your request...")
                webbrowser.open(site[1])
def get_ip(_return=False):
    try:
        response = requests.get(f'http://ip-api.com/json/').json()
        if _return:
            return response
        else:
            return f'Your IP address is {response["query"]}'
    except KeyboardInterrupt:
        return None
    except requests.exceptions.RequestException:
        return None