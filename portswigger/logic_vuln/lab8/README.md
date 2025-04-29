# Lab: Insufficient workflow validation

description : This lab makes flawed assumptions about the sequence of events in the purchasing workflow.

End goal : To solve the lab, exploit this flaw to buy a `"Lightweight l33t leather jacket"`.

creds : `wiener:peter`

## Analysis

- trying to manipulate the quantity parameter -> no reuslts
- following the multi-stage purchasing functionality via low price product and saving the final request
- and re-sending the final request after adding the jacket to the cart -> actually buying it

## Mitigation

- before acutally check out the user -> check if he have completed the previous stages
