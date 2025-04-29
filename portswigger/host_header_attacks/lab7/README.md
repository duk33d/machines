# Lab: Host validation bypass via connection state attack

Description :
This lab is vulnerable to routing-based SSRF via the Host header. Although the front-end server may initially appear to perform robust validation of the Host header, `it makes assumptions about all requests on a connection based on the first request it receives`.

End Goal :
To solve the lab, exploit this behavior to access an internal admin panel located at `192.168.0.1/admin`, then delete the user `carlos`.

Analysis :

- Sending the malicious request direct -> 301 Moved Permanently
- using the hint provided by portswigger -> the solution is making a group  contains 2 requests
  - the first one is legit & the second is mal
  - sending the group in single connection  -> passes
