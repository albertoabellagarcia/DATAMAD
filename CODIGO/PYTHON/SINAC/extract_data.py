from bs4 import BeautifulSoup
import os
import json


def echo(variablename, variable):
    print("____________________________")
    print(variablename + " = " + str(variable))
    print("*****************************")


def cleanhtml(text):

    output = text
    cleandict = [
        {"chain": "\\xc3\\xad", "replacement": "i"},
        {"chain": "\\xc3\\xa1", "replacement": "a"},
        {"chain": "\\xc3\\xa9", "replacement": "e"},
        {"chain": "\xc3\xa1", "replacement": "e"},
        {"chain": "\xc3\xb3", "replacement": "o"},
        {"chain": "\\xc3\\xb3", "replacement": "o"},
        {"chain": "\\t", "replacement": ""},
        {"chain": "\\r", "replacement": ""}

    ]
    for element in cleandict:
        if element["chain"] in text:
            output = output.replace(element["chain"], element["replacement"])

    return output


# main repository of information
sinac = {"data": {}, "date": "18/04/2024"}

# where the retrieved pages are store for late processing
mypath = "./pages2024"

# codes of the tables where the analysis information is contained
tableCodes = ["rowIndic", "rowMicro", "rowPlag", "rowQuim"]

# files with the source code of the pages
onlyfiles = [f for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

outputFileSinac = "sinac2024.json"

for fileInDir in onlyfiles:
    echo("fileInDir", fileInDir)
    index = fileInDir.replace("page", "").replace(".html", "")
    # reading the source page file
    with open(mypath + "/" + fileInDir, "r") as file:
        content = file.read()[2:]
    print(content)
    soup = BeautifulSoup(content, 'html.parser')
    echo("soup", soup)

    # looking for the main data of the water source
    sinac["data"][index] = {}
    sourceKeys = []
    sourceValues = []
    mainDataHtml = soup.find("div", attrs={"class": "bloqueTabla"})
    if mainDataHtml is None:
        continue
    mainDataHeader = mainDataHtml.findAll("th")

    # retrieve the headers of the main data about the water data source
    for item in mainDataHeader:
        sourceKeys.append(cleanhtml(str(item.text)))
        print(sourceKeys[:-1])
    # retrieve the values of the main data about of the water data source
    mainDataRows = mainDataHtml.findAll("td")
    for item in mainDataRows:
        sourceValues.append(cleanhtml(str(item.text)))
        print(sourceValues[:-1])
    # create the dict to attached to the output
    sourceDict = dict(zip(sourceKeys, sourceValues))

    sinac["data"][index] = sourceDict
    print(sourceDict)

    # looking for the analysis tables of the water source in the source code
    sinac["data"][index]["analisis"] = []
    analysis = {}
    for table in tableCodes:
        print("table = " + table)
        tableHtml = soup.find("table", attrs={"id": table})
        echo("tableHtml", tableHtml)

        # some pages have not tables
        if tableHtml is None:
            print("table " + table + "is not found at file " + fileInDir)
            analysis["type"] = table
            analysis["data"] = "Not available"
        else:
            analysis = {"type": table, "data": []}
            # some other they do
            tableHtmlData = tableHtml.find_all("tr")
            heading = []
            echo("tableHtmlData", tableHtmlData)
            for td in tableHtmlData[0].find_all("th"):
                echo("td", td)
                # getting headers
                heading.append(cleanhtml(str(td.text)))
            echo("heading", heading)
            values = []
            for row in tableHtmlData[1:]:
                echo("row", row)
                # remove any newlines and extra spaces from left and right
                rowValues = row.find_all("td")
                echo("rowValues", rowValues)
                values = []
                for value in rowValues:
                    values.append(cleanhtml(str(value.text)))
                echo("values", values)
                row = {}
                for counter, element in enumerate(values):
                    echo("element", element)
                    echo("counter", counter)
                    echo("heading[counter]", heading[counter])
                    row[heading[counter]] = element
                analysis["data"].append(row)
            sinac["data"][index]["analisis"].append(analysis)
            echo("analysis", analysis)

with open(outputFileSinac, "w") as sinacFile:
    sinacFile.write(json.dumps(sinac))
