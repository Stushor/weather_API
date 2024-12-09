import requests


ARTICLE_ID = ['svo', 'london', 'cherepovets']


def main():
    for article in range(len(ARTICLE_ID)):
        url_template = 'https://wttr.in/{}?nTqM&lang=ru'
        url = url_template.format(ARTICLE_ID[article])
        response = requests.get(url)
        response.raise_for_status()
        print(response.text)


if __name__ == '__main__':
    main()
