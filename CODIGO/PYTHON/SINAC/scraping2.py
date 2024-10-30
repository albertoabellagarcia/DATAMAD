# this file retrieves teh pages that later are parse in local files (23000)
import requests

limit = 23000
for i in range(limit):
    print(limit-i)
    url = "https://sinacv2.sanidad.gob.es/CiudadanoWeb/ciudadano/informacionAbastecimientoActionCA.do?idRed=" + str(i)
    page = requests.get(url)
    filePath = "pages2024/page" + str(i) +".html"
    with open(filePath, "w") as file:
        file.write(str(page.content))


