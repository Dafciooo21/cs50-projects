import requests
import json
import sys

response = requests.get("https://www.brickeconomy.com/set/40560-1/lego-brickheadz-wizarding-world-professors-of-hogwarts")

print(response)
