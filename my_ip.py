import requests
import re

def get_my_ip(url='http://www.cualesmiip.com/', proxies=None):
    try:
        r = requests.get(url=url, proxies=proxies)
    except Exception as e:
        print('Error haciendo la request', e)
        return None

    if r.status_code != 200:
        print("Status Code:", r.status_code)
        return None

    regex = re.compile(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    my_ip = regex.findall(r.text)
    return my_ip[0] if my_ip else None

if __name__ == "__main__":
    print(get_my_ip())