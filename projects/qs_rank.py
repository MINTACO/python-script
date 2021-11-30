import requests


def main():
    r = requests.get('https://www.topuniversities.com/sites/default/files/qs-rankings-data/en/3740566.txt?1638264782?v=1638270639954')
    print(r.json())

