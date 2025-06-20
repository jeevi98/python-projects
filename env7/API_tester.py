import requests
import json
from datetime import datetime

def log_to_file(log_data, log_file="api_log.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(log_data + "\n" + ("-"*60) + "\n")

def send_request(method, url, headers=None, payload=None):
    try:
        response = requests.request(method, url, headers=headers, json=payload)

        log_entry = f"""[ {datetime.now()}]
 URL: {url}
 Method: {method}
 Request Body: {json.dumps(payload, indent=2) if payload else "None"}
 Status Code: {response.status_code}
 Headers: {dict(response.headers)}
 Response Body: {response.text}
"""
        print(log_entry)
        log_to_file(log_entry)
        
    except requests.exceptions.RequestException as e:
        error_log = f" Request failed: {e}"
        print(error_log)
        log_to_file(error_log)

def main():
    print(" REST API Tester\n")

    method = input("Enter HTTP method (GET, POST, PUT, DELETE): ").strip().upper()
    if method not in ["GET", "POST", "PUT", "DELETE"]:
        print(" Invalid method.")
        return

    url = input("Enter full API URL: ").strip()
    headers_input = input("Enter headers as JSON (or leave blank): ").strip()
    payload_input = input("Enter body as JSON (for POST/PUT) or leave blank: ").strip()

    headers = json.loads(headers_input) if headers_input else None
    payload = json.loads(payload_input) if payload_input and method in ["POST", "PUT"] else None

    send_request(method, url, headers, payload)

if __name__ == "__main__":
    main()
