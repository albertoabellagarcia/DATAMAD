import os
import re
import asyncio
import aiohttp


# Function to asynchronously request a web page and return its content
async def fetch_url(session, url):
    try:
        async with session.get(url) as response:
            content = await response.text()  # Get full content as text
            return url, response.status, content
    except aiohttp.ClientError as e:
        return url, None, str(e)


# Fetch multiple URLs asynchronously
async def fetch_urls_in_parallel(url_list):
    results = []
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in url_list]
        for task in asyncio.as_completed(tasks):
            url, status_code, content = await task
            index = url.replace(
                "https://sinacv2.sanidad.gob.es/CiudadanoWeb/ciudadano/informacionAbastecimientoActionCA.do?idRed=", "")
            results.append((url, status_code, content))

            filePath = "pages2024/page" + index +".html"
            with open(filePath, "w") as file:
                file.write(str(content))
            print(f"Fetched {index} source: Status Code {status_code}, Content Length {len(content) if content else 0}")
    return results

# List of URLs to fetch



# Function to extract numbers from filenames with the pattern 'pageNN.html'
def extract_numbers_from_filenames(directory):
    pattern = re.compile(r'page(\d+)\.html')  # Regular expression to match 'pageNN.html'
    numbers = []

    # List all files in the directory
    for filename in os.listdir(directory):
        match = pattern.match(filename)
        if match:
            numbers.append(int(match.group(1)))  # Extract the number and convert to integer

    return numbers

directory = "./pages2024"
retrieved_sources = extract_numbers_from_filenames(directory)
retrieved_urls = ["https://sinacv2.sanidad.gob.es/CiudadanoWeb/ciudadano/informacionAbastecimientoActionCA.do?idRed=" + str(i) for i in retrieved_sources]

limit = 23000
initial_urls = ["https://sinacv2.sanidad.gob.es/CiudadanoWeb/ciudadano/informacionAbastecimientoActionCA.do?idRed=" + str(i) for i in range(23000)]

urls = [url for url in initial_urls if url not in retrieved_urls]

print("the remaining urls " + str(len(urls)))
# Run the async event loop
fetched_pages = asyncio.run(fetch_urls_in_parallel(urls))

