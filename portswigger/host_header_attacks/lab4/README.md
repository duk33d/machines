# Lab: Host header authentication bypass

Description :
This lab makes an assumption about the privilege level of the user based on the HTTP Host header.

End Goal : access the admin panel and delete the user carlos.

Analysis:

- /robots.txt exposes `/admin`
- the vulnerable server accepts arbtirary host header values
- direct access to `/admin` returns -> 401 unauthorized
- GET `/admin` while changing host header -> local host -> 200 OK   // Lab solved
