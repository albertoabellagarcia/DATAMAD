import shapefile

# Path to the shapefile
filepath = 'IDEM_MA_FISIOGRAFIA_50M.zip'

# Try different encodings
encodings = ['ISO8859-1', 'CP1252', 'Latin-1']

for encoding in encodings:
    try:
        sf = shapefile.Reader(filepath, encoding=encoding)
        records = sf.records()
        print(f"Successfully read records using {encoding} encoding")
        break
    except UnicodeDecodeError:
        print(f"Failed to read records using {encoding} encoding")
        continue
