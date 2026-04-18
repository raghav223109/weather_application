import requests

def get_location():
    try:
        res = requests.get("https://ipinfo.io").json()
        return res.get("city", "Delhi")
    except:
        return "Delhi"