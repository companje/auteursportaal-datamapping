# mapping toepassen van Excel data in CSV naar linked data in Turtle

EXCEL_FILE=data/excel/Schrijvers_Operaasje_Fers_V2-1.xlsx
CSV_FILE=data/excel/Schrijvers_Operaasje_Fers_V2-1.csv
TURTLE_FILE=data/result/schrijvers.ttl

# first convert Excel to CSV
./xlsx2csv.py --input $EXCEL_FILE --output $CSV_FILE

# then map CSV to Turtle
./mapping.py \
  --input=$CSV_FILE \
  --header=data/templates/Header.ttl \
  --template=data/templates/Schrijver.ttl \
  --output=$TURTLE_FILE \
  --limit=500000

echo $TURTLE_FILE