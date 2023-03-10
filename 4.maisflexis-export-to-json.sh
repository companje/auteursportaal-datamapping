# converteer het Export XML bestand van MaisFlexis naar JSON
# dit script wordt op een webserver uitgevoerd

URL=http://mfxml2json.0x03.nl:8888/run
INPUT_FILE=data/maisflexis/nieuw-A0003_14_158_flexis.txt
OUTPUT_FILE=data/maisflexis/nieuw-A0003_14_158_flexis.json
curl -J -X POST -F "file=@$INPUT_FILE" $URL > $OUTPUT_FILE

echo $OUTPUT_FILE