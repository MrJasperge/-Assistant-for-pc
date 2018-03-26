import json

with open('intents.json', 'r') as r:
  intents = json.load(r)

def execute(text):
  print("execute")
