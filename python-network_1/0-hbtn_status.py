#!/usr/bin/python3
"""
fetch https://alu-intranet.hbtn.io/status; display response
"""

import urllib.request

def fetch_status(url):
    """
    Fetches the status from the specified URL using urllib.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        None: The function prints the body response or error information.
    """
    try:
        # Open the URL using urllib and create a context manager with 'with'
        with urllib.request.urlopen(url) as response:
            # Read the content of the response and decode it
            body = response.read().decode('utf-8')
            
            # Display the body response information
            print("Body response:")
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")

    except urllib.error.HTTPError as e:
        # Handle HTTP errors
        print(f"Error code: {e.code}")

    except urllib.error.URLError as e:
        # Handle URL errors
        print(f"Error: {e.reason}")

# Example usage
url = "https://alu-intranet.hbtn.io/status"
fetch_status(url)
