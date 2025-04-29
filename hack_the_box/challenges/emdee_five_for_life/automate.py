import requests
import urllib3
import sys
from bs4 import BeautifulSoup
import hashlib
# some times work / sometime returns the flag



proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def main (host:str):
    s = requests.Session()

    reponse = s.get(host )
    soup = BeautifulSoup(reponse.content,'html.parser')

    hashed_value = hashlib.md5(soup.find('h3').text.encode('utf-8')).hexdigest()
    params={"hash":hashed_value}

    response = s.post(host,data=params,)
    print(response.text)

    print(hashed_value)

if __name__=="__main__":
    if sys.argv !=2:
        print("(-) Usage : http://ip:port ")
        #exit()
    host = sys.argv[1]
    main(host)
