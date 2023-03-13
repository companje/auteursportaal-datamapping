from liquid import Liquid
import json,csv,hashlib,re,sys
from datetime import datetime
from rdflib import Graph, Literal
from tqdm import tqdm

def data_mapping(input_filename, header_filename, template_filename, output_filename, limit=0):
  items = load_items(input_filename)

  if limit>0:
    items = items[:limit]

  filters = {
      "make_safe_literal": make_safe_literal,
      "is_valid_isodate": is_valid_isodate,
      "md5": md5,
      "lat": get_latitude,
      "lon": get_longitude
  }

  ttl = open(header_filename).read()

  for item in tqdm(items):
    ttl += apply_liquid_template(
        replace_keys_by_values(template_filename, item), 
        make_safe_keys(item),
        filters=filters
      ) + "\n"

  g = Graph()
  g.parse(data=ttl)
  g.remove((None, None, Literal(""))) #remove triples with empty literals
  with open(output_filename,"w") as f:
    print(g.serialize(),file=f)

def make_safe_literal(s): # replace single " quote by double "" and add quotes
  s = s.strip()
  s = re.sub(r"\n", "\\\\n", s)
  s = re.sub(r"\"", "\\\"", s)
  return s

def make_safe_URI_part(s):
  # spreadsheet: [–’&|,\.() ""$/':;]"; "-") ;"-+";"-"); "[.-]$"; ""))
  s = re.sub(r"[–’+?&=|,\.() \"$/']", "-", s) # replace different characters by a dash
  s = re.sub(r"-+", "-", s) # replace multiple dashes by 1 dash
  s = re.sub(r"[^a-zA-Z0-9\-]", "", s) # strip anything else now that is not a alpha or numeric character or a dash
  s = re.sub(r"^-|-$", "", s) # prevent starting or ending with . or -
  if len(s)==0:
    #raise ValueError("makeSafeURIPart results in empty string")
    # log.warning("makeSafeURIPart results in empty string")
    # fix this by replacing by 'x' for example
    s="x"
  return s.lower()

def get_latitude(s):
  try:
    lat,lon = re.findall(r"([\d\.]+),\s*([\d\.]+)",s)[0]
    return lat
  except:
    return ""
 
def get_longitude(s):
  try:
    lat,lon = re.findall(r"([\d\.]+),\s*([\d\.]+)",s)[0]
    return lon
  except:
    return ""

def make_safe_key_name(s): # for Liquid templates
  return s.replace(' ', '_').replace('?','')

def make_safe_keys(item):
  return { make_safe_key_name(x): v for x, v in item.items() } # renames keynames to use in template

def replace_keys_by_values(s,item,start="{{",end="}}"):
  for key in item:
       s = s.replace(f"{start}{key}{end}", str(item[key]))
  return s

def apply_liquid_template(template_filename, item, filters={}):
    return Liquid(template_filename, liquid_from_file=True, filters=filters).render(**item)

def load_json_items(filename):
    return json.load(open(filename, encoding='utf-8-sig'))

def load_csv_items(filename, delimiter=","):
    return list(csv.DictReader(open(filename, encoding='utf-8-sig'), delimiter=delimiter))

def load_items(filename):
  if filename.endswith(".csv"):
    return load_csv_items(filename)
  elif filename.endswith(".json"):
    return load_json_items(filename)
  else:
    sys.exit(f"unknown file type: {filename}")

def md5(s):
    return hashlib.md5(s.encode()).hexdigest()

def is_valid_isodate(dt_str):
  try:
    datetime.fromisoformat(dt_str)
    return True
  except:
    return False
