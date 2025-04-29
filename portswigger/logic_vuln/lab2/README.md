# Lab: 2FA broken logic

Description : This lab's two-factor authentication is vulnerable due to its flawed logic.

End goal : To solve the lab, access Carlos's account page.

creds : `wiener:peter` , victim's username `carlos`

Analysis :

- the back end system maps the provided OTP to the user provided in cookie `verify`
- there is no limits on the OTP , which leavs it vlnerable to brute forcing
