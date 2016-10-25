import os
import json
a = []

for f in os.listdir("./ImageData/"):
    if f.endswith(".jpg"):
    	a.append(f)

print(json.dumps(a))
