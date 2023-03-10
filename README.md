# Install
1. Clone this repo
2. ```pip install -r requirements.txt```

# Usage
1. download data using the Omeka API.
```
./1.omeka-harvest.py
```

2. convert ±225 JSONLD files from Omeka to a single Turtle file
```
./2.omeka-jsonld-to-turtle.py
```

3. optional: add extra titles as schema:name and thumbnails as schema:image. this makes navigating in the triply browser easier.
```
./3.omeka-extract-titles-thumbnails-(optional).py
```

4. convert mais mfxml-export file to a list of json objects. (executed remotely)
```
./4.maisflexis-export-to-json.sh
```

5. use liquid templates to format Turtle files with values from JSON ('Collectie-Operaesje-Fers')
```
./5.maisflexis-mapping-json-to-turtle.sh
```

6. use liquid templates to format Turtle files with values from CSV ('Schrijvers')
```
./6.excel-mapping-csv-to-turtle.sh
```
