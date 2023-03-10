#!/usr/bin/env python3

import argparse
from utils import *
from rdflib import Graph, Literal

parser=argparse.ArgumentParser()
parser.add_argument("--input", help="input CSV or JSON file", required=True)
parser.add_argument("--header", help="Turtle file containing @prefix statements", required=True)
parser.add_argument("--template", help="Turtle template per item type in input file. For example: templates/{{KEY_NAME}}.ttl or templates/SingleType.ttl", required=True)
parser.add_argument("--output", help="output Turtle file", required=True)
parser.add_argument("--limit", type=int, help="limit number of items for increased speed during testing")
args=parser.parse_args()

items = load_items(args.input)

if args.limit:
    items = items[:args.limit]

filters = {
    "make_safe_literal": make_safe_literal,
    "is_valid_isodate": is_valid_isodate,
    "md5": md5
}

ttl = open(args.header).read()
ttl += apply_liquid_templates(items=items, template_filename=args.template, filters=filters)

g = Graph()
g.parse(data=ttl)
g.remove((None, None, Literal(""))) #remove triples with empty literals
with open(args.output,"w") as f:
	print(g.serialize(),file=f)

