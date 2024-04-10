# Get the IP address and the IP Address Information
import requests
from parsel import Selector
def get_data():
    try:
        data = requests.get('http://checkip.dyndns.com/').text
        selector = Selector(text=data)
        ipaddress= (selector.css('body::text').get()).split('Address: ')[1].strip()
        if not ipaddress:
            print("Error getting IP Address")
            return
        response = requests.get(f'http://ip-api.com/json/{ipaddress}').json()
        if response['status'] == 'fail':
            print("Error getting IP Address Information")
            return
        print("IP Address Information")
        print(f'IP Address: {response["query"]}\nCountry: {response["country"]}\nCountry Code: {response["countryCode"]}\nCity: {response["city"]}\nRegion: {response["regionName"]}\nLatitude: {response["lat"]}\nLongitude: {response["lon"]}\nISP: {response["isp"]}\nOrganization: {response["org"]}\nAS: {response["as"]}')
    except Exception as e:
        print(f"Error: {e}")
        return

if __name__ == '__main__':
    # get_data()
    get_data()