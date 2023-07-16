import requests

def get_proxy(count):
    url = f"https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    response = requests.get(url)
    if response.status_code == 200:
        proxies = response.text.split('\n')
        return proxies[:count]
    else:
        print("Error:", response.status_code)
        return None

def write_to_file(proxies):
    with open('proxies.txt', 'w') as f:
        for proxy in proxies:
            if proxy:
                f.write(proxy)

count = int(input("How many proxies do you want to generate? "))
proxy_list = get_proxy(count)
write_to_file(proxy_list)