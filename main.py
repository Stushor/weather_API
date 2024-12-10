import requests


PLACES = ['svo', 'london', 'cherepovets']


def main():
    payload = {"n": "",
               "T": "",
               "q": "",
               "M": "",
               "lang": "ru"}
    for place in PLACES:
        url_template = 'https://wttr.in/{}'
        url = url_template.format(place)
        response = requests.get(url, params=payload)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
