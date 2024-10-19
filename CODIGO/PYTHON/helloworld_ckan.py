# Este programa es una ejemplo básico del uso del paquete ckanapi para la recuperación de datos de un portal basado en ckan como el de la comunidad de madrid

from ckanapi import RemoteCKAN

# Connect to the CKAN instance
ckan = RemoteCKAN(': http://datos.comunidad.madrid/')

# Fetch a dataset (using the dataset ID or name)
dataset = ckan.action.package_show(id='93bed3f0-3ba5-4b00-90bf-1c81951bab24')


# Print dataset details
print(dataset)

# Search datasets
result = ckan.action.package_search(q='aire')
#
# # Create or update a dataset (authenticated with an API key)
# ckan_with_key = RemoteCKAN('https://your-ckan-instance-url.com', apikey='your-api-key')
# ckan_with_key.action.package_create(name='new-dataset', title='New Dataset Title')
