# Lab: Excessive trust in client-side controls

Description : This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price.

End Goal : To solve the lab, buy a "Lightweight l33t leather jacket".

creds : `wiener:peter`

analysis:

- the application accept arbitrary not necessary user input without validating it properly
  - by changing the price from 133700 -> to 100 -> we could but it by 1.00$ dollar
