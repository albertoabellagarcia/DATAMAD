################################################################################
#  File under the Apache License, Version 2.0 (the
#  "License"); you may not use this file except in compliance
#  with the License.  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
# limitations under the License.
################################################################################

# Este fichero extrae el listaod de datasets del portal de datos abiertos de la comunidad de Madrid
# version 0.4

# Importamos dos librerías básicas
import json
import requests
import sys

# url base  del API del portal de datos de la comunidad de Madrid
# tenemos que incluir el parametro limit por que por defecto nos da 20 recursos
base_url = "http://datos.comunidad.madrid/api/3/action/current_package_list_with_resources?limit=300"

# Realizamos la petición
result = requests.get(base_url)

# Si el resultado es exito de la conexión cargamos los resultados en una variable
if result.status_code == 200:
    catalogue_dict = json.loads(result.text)["result"]

# Listamos los resultados
for item in catalogue_dict:
    print(item)

# Guardamos el catalogo en un fichero llamado "full_catalogue.json"
with open("full_catalogue.json", "w") as file:
    json.dump(catalogue_dict, file, indent=2)

# Contar cuantos datasets se han creado por año
annos = {}

# revisamos cada uno de los datasets
for item in catalogue_dict:
    print("El datasets " + item["title"] + " tiene " + str(len(item["resources"])) + " distribuciones")
    # cada dataset puede tener varios recursos (distribuciones) que se pueden crear en fechas distintas
    for resource in item["resources"]:
        print(resource)
        # Extraemos el año de creación del dataset
        anno = resource["created"][:4]
        print(anno)
        print(type(anno))
        if anno in annos:
            # Si ya hay más de ese año lo añadimos
            annos[anno] += 1
        else:
            # Si es el primero del año creamos la entrada
            annos[anno] = 1

print(annos)
for anno, value in annos.items():
    print("El año " + str(anno) + " se crearon " + str(value) + " distribuciones")

annos_datasets = {}
for item in catalogue_dict:
# accedemos a la fecha de creación del dataset
    anno = item["metadata_created"][:4]
    if anno in annos_datasets:
        # Si ya hay más de ese año lo añadimos
        annos_datasets[anno] += 1
    else:
        # Si es el primero del año creamos la entrada
        annos_datasets[anno] = 1

print(annos_datasets)
for anno, value in sorted(annos_datasets.items()):
    print("El año " + str(anno) + " se crearon " + str(value) + " datasets")
