import urllib.request
import json
import sys

TOKEN = "hLMaj4GuN3QsAum1bZmVR+r+57X/QbUeH/XqmO7FkpaVW9mmKfTAsH4u6G4LozwjYCRnQaR0cXMNrbvjnaZl4yDZcsM7e31pwvK38GxM7WzWffgaxz7CSP4tY7Edh/g4znkyvLx0DN2ITkXqLhDpGAdB04t89/1O/w1cDnyilFU="

req = urllib.request.Request("https://api.line.me/v2/bot/richmenu/list")
req.add_header("Authorization", f"Bearer {TOKEN}")

try:
    with urllib.request.urlopen(req) as response:
        data = json.loads(response.read().decode())
        print(json.dumps(data, indent=2, ensure_ascii=False))
except Exception as e:
    print(e)
    if hasattr(e, 'read'):
        print(e.read().decode())
