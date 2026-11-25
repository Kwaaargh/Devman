import requests

GPS_COORDINATES = {
    "Сан-Франциско": "37.77493,-122.41942",
    "Лондон": "51.50853,-0.12574",
    "Аэропорт Шереметьево (SVO)": "55.97250,37.41306",
    "Череповец": "59.13333,37.90000",
}
urls = []
for coordinate in GPS_COORDINATES.values():
    raw_url = "https://wttr.in/{}?nTqu&lang=en".format(coordinate)
    urls.append(requests.get(raw_url))

for url in urls:
    try:
        url.raise_for_status()
        print(url.text)
    except requests.HTTPError:
        print("Адрес не вернул результат")
