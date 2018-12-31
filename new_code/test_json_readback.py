import json

# reads it back
with open("4forces.json","r") as f:
  d = json.load(f)

print("reading back")
print(d)
