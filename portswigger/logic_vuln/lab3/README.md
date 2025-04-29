# Lab: High-level logic vulnerability

Description : This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price.

End Goal : To solve the lab, buy a `"Lightweight l33t leather jacket"`.

creds : `wiener:peter`

Analysis :

- notice the request that updates the quentatity and infer that u might try to add negative values , to pay less than what u should be paying
- trying to add negative quantity -> so get mony is rejected by the overall price is must be not negative
- what about adding negative quantities to make the real price less than the legimate one ? -> congrats u have solved the lap
