#!/usr/bin/env python3

from pathlib import Path
from rdflib import Graph, Literal, Namespace, URIRef

input_files = list(Path("data/omeka").rglob("*.json"))
output_filename = "data/result/omeka.ttl"

g = Graph()
g.bind("o", Namespace("http://omeka.org/s/vocabs/o#"))
g.bind("rdfs", Namespace("http://www.w3.org/2000/01/rdf-schema#"))
g.bind("dcterms", Namespace("http://purl.org/dc/terms/"))
g.bind("dctype", Namespace("http://purl.org/dc/dcmitype/"))
g.bind("bibo", Namespace("http://purl.org/ontology/bibo/"))
g.bind("foaf", Namespace("http://xmlns.com/foaf/0.1/"))
g.bind("schema", Namespace("http://schema.org"))
g.bind("edm", Namespace("http://www.europeana.eu/schemas/edm/"))
g.bind("RiCo", Namespace("https://www.ica.org/standards/RiC/ontology"))
g.bind("o-cnt", Namespace("http://www.w3.org/2011/content#"))
g.bind("o-time", Namespace("http://www.w3.org/2006/time#"))
g.bind("o-module-mapping", Namespace("http://omeka.org/s/vocabs/module/mapping#"))

# add all json files to one graph
for input_file_path in input_files:
    print(input_file_path)
    g.parse(input_file_path)

# write graph to turtle file
ttl = g.serialize(format="ttl")
ttl = ttl.replace("<schema:>", "<http://schema.org/>") #fix invalid schema prefix
print(ttl,file=open(output_filename,"w"))
print(output_filename)

