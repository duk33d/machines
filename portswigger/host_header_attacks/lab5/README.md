# Lab: Routing-based SSRF

Description :
This lab is vulnerable to routing-based SSRF via the Host header. You can exploit this to access an insecure intranet admin panel located on an internal IP address.

End goal:
To solve the lab, access the internal admin panel located in the `192.168.0.0/24` range, then delete the user `carlos`.

Analysis:

- sending simple get request using `Host: test`
  - returns -> `Server Error: Gateway Timeout (3) connecting to test`
  - brute forcing the internal ips -> ip 192.168.0.159 -> 302 redirect
