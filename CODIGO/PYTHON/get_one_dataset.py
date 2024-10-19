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

# url base  del API del portal de datos de la comunidad de Madrid
# tenemos que incluir el parametro limit por que por defecto nos da 20 recursos
base_url = "http://datos.comunidad.madrid/api/3/action/package_show?id=3dacd589-ecca-485c-81b9-a61606b7199f"

# Realizamos la petición
result = requests.get(base_url)

# Si el resultado es exito de la conexión cargamos los resultados en una variable
if result.status_code == 200:
    dataset_dict = json.loads(result.text)["result"]

# Now we get the json distribution
for resource in dataset_dict["resources"]:
    if resource["format"].lower() == "json":
        json_distribution_url = resource["url"]
        distribution_pointer = requests.get(json_distribution_url)
        if distribution_pointer.status_code == 200:
            distribution = json.loads(distribution_pointer.text)

print(json.dumps(distribution, indent=2))

