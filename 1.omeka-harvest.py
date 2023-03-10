#!/usr/bin/env python3
import requests, json

types = [
  "api_resources",
  "assets",
  "csvimport_entities",
  "csvimport_imports",
  "custom_vocabs",
  "data_types",
  "item_sets",
  "items",
  "jobs",
  "mapping_markers",
  "mappings",
  "media",
  "modules",
  "properties",
  "resource_classes",
  "resource_templates",
  "resources",
  "site_pages",
  "sites",
  "users",
  "value_annotations",
  "vocabularies"
]

for t in types:
  page = 1
  url = "https://tresoar.omeka.net/api/"+t
  while url:
      print(url)
      response = requests.get(url)
      filename = f"data/omeka/{t}-{page}.json"
      json.dump(response.json(), open(filename,"w"), indent=2)
      next = response.links.get("next")
      url = next["url"] if next else ""
      page += 1
