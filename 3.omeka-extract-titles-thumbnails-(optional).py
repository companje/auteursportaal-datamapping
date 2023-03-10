#!/usr/bin/env python3

from pathlib import Path
from rdflib import Graph, Literal, Namespace, URIRef

input_file = "data/result/omeka.ttl"
output_file = "data/result/omeka-titles-thumbnails.ttl"

g = Graph()
g.parse(input_file)
titles = Graph()

# add rdfs:title triples
preds = [
	URIRef("http://omeka.org/s/vocabs/o#title"),
	URIRef("http://omeka.org/s/vocabs/o#label"),
	URIRef("http://schema.org/title")
]

for pred in preds:
    for subj,_,obj in g.triples((None, pred, None)):
        titles.add((subj, URIRef("https://schema.org/name"), obj))

# add thumbnail images
for subj,_,obj in g.triples((None, URIRef("http://omeka.org/s/vocabs/o#source"), None)):
	obj = Literal(str(obj).replace("/info.json","/full/,200/0/default.jpg"))
	titles.add((subj, URIRef("https://schema.org/image"), obj))

# print titles graph to file
print(titles.serialize(format="ttl"),file=open(output_file,"w"))
print(output_file)