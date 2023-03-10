# mapping toepassen van MF data in JSON naar linked data in Turtle

JSON_FILE=data/maisflexis/nieuw-A0003_14_158_flexis.json
TURTLE_FILE=data/result/Collectie-Operaesje-Fers.ttl

./mapping.py \
  --input=$JSON_FILE \
  --header=data/templates/Header.ttl \
  --template=data/templates/{{Soort}}.ttl \
  --output=$TURTLE_FILE \
  --limit=500000 \

# optional thumbnail images for Example Resources
echo 'id:808425 schema:image "https://www.sirkwy.frl/images/404mwajlbdp9osv.jpg" .' >> $TURTLE_FILE
echo 'id:cf393a46126324b40fe9de4ccf005feb schema:image <https://wiki-thumb.hualab.nl/Q2143934> .' >> $TURTLE_FILE
echo 'id:842206 schema:image "https://www.sirkwy.frl/images/nijs/Operaesje.jpg" .' >> $TURTLE_FILE

echo $TURTLE_FILE
