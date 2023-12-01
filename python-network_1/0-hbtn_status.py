#!/usr/bin/python3
"""
fetch https://alu-intranet.hbtn.io/status; display response
"""

import urllib.request

url = "https://alu-intranet.hbtn.io/status"

try:
    with urllib.request.urlopen(url) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
