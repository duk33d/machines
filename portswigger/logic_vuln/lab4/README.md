# Lab: Low-level logic flaw

Description : This lab doesn't adequately validate user input. You can exploit a logic flaw in its purchasing workflow to buy items for an unintended price.

End goal : To solve the lab, buy a "Lightweight l33t leather jacket".

Creds : `wiener:peter`

## Analysis

- trying to add quantity more thatn 100 -> returns error
- so adding multiple quantity=99 -> makes the variable which holds the value of total bill overflows -> negative value
  - [integer values](https://hpccsystems.com/wp-content/uploads/_documents/ECLR_EN_US/INTEGER.html)
  - searched for maximu interger values , because when i tried to add float qunatity it returned data type error as i entered string
- adding another valued to make it more than 0 and less than `100$`

## Mitigation

- the bug here is the back end developer is not checking the maximum overall quantity
- if the back end said that
  - the maximum quantity per BILL Is 100 for example and checked the quantity in the database to see if it under the limit or not -> there is no bug
- or checking the overall bill price is a better solution i think , like the maximum value price per BILL shouldn't exceed 10,000$ For example
