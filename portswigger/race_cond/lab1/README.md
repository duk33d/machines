# Lab: Limit overrun race conditions

Description : This lab's purchasing flow contains a race condition that enables you to purchase items for an `unintended price`.

Goal :  successfully purchase a `Lightweight L33t Leather Jacket`.

Creds: `wiener:peter`

Analysis:

- The logic in applying `20% off` using the promo code is based on ratio
  - it just removing `20%` of the current total price
- testing for race condtion vulnerable
- by trial and error the needed amount of requests 21 request -> to make the total price of bill below 50$ ( provided by the lab)
  - intercept the request of applying promo code & create tab group
  - duplicate the tab & chose Send group (parallel)
  - might not work from the first time (depends on not controlled variables) , but eventually will work -> lab solved
