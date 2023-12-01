#!/usr/bin/python3
"""
fetch https://alu-intranet.hbtn.io/status; display response
"""

import urllib.request
from contextlib import closing

url = "https://alu-intranet.hbtn.io/status"

try:
    with closing(urllib.request.urlopen(url)) as response:
        body = response.read().decode('utf-8')
        print(f"Body response:\n\t- type: {type(body)}\n\t- content: {body}")
except urllib.error.HTTPError as e:
    print(f"Error code: {e.code}")
except urllib.error.URLError as e:
    print(f"Error: {e.reason}")
