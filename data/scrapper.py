import requests as rq
from bs4 import BeautifulSoup
base_path ="https://www.plusvalia.com/venta/casas"

path_cities = [
    "pichincha/quito",
    "guayas/guayaquil",
    "manabi/manta"
]

city = path_cities[0]
request = rq.get(f"{base_path}/{city}")

if request.status_code == 200:
    html = request.text
    soup = BeautifulSoup(html, "lxml")
    print(soup.prettify())
else:
    pass
    