import json

with open('intents.json', 'r') as r:
  intents = json.load(r)

for intent in intents:
  for keyword in intents[intent]:
    print(intent, keyword)
