# Lab: Basic password reset poisoning

This lab is vulnerable to password reset poisoning. The user carlos will carelessly click on any links in emails that he receives. To solve the lab, log in to Carlos's account.

You can log in to your own account using the following credentials: wiener:peter. Any emails sent to this account can be read via the email client on the exploit server.

Analysis:

- the back-end server sends token to the user email to reset their password
- by mmanipulating the host header with our own domain the back end uses our domain instead of the legimate domain
- extracting the token from the logs -> 1 click ATO
Another scenario :
- we might use headers that should override the host header for example :
  - X-Forwarded-For header or other header that would function as it
