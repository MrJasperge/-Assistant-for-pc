import commands
import query_parser
import json

with open('intents.json', 'r') as r:
  intents = json.load(r)

