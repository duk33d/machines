# Lab: Flawed enforcement of business rules

Description : This lab has a logic flaw in its purchasing workflow.

End goal : To solve the lab, exploit this flaw to buy a `"Lightweight l33t leather jacket"`.

creds : `wiener:peter`

## Analysis

- `NEWCUSTS` is general code with all new members
- after signing up in the newsletter gets another code `SIGNUP30`
- trying to apply the same code twice in row -> returns code already applied
- but when mixing it , 1- newcusts , 2- signup30 , 3- newcusts , ...
- works  till total bil become 0.00

## Mitigation

- create a table with one to many relationship between cart and codes (forign keys)
- keep track of used codes and check if the applied code is alredy used  or not
