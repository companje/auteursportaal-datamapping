# Install
1. Clone this repo
2. ```pip install -r requirements.txt```

# Usage
```
./1.omeka-harvest.py
```
download data using the Omeka API.

```
./2.omeka-jsonld-to-turtle.py
```
convert ±225 JSONLD files from Omeka to a single Turtle file

```
./3.omeka-extract-titles-thumbnails-(optional).py
```
optional: add extra titles as schema:name and thumbnails as schema:image. this makes navigating in the triply browser easier.

```
./4.maisflexis-export-to-json.sh
```
convert mais mfxml-export file to a list of json objects. (executed remotely)

```
./5.maisflexis-mapping-json-to-turtle.sh
```
use liquid templates to format Turtle files with values from JSON ('Collectie-Operaesje-Fers')

```
./6.excel-mapping-csv-to-turtle.sh
```
use liquid templates to format Turtle files with values from CSV ('Schrijvers')
