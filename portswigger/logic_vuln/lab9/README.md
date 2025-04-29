# Lab: Authentication bypass via flawed state machine

Description : This lab makes flawed assumptions about the sequence of events in the login process.

End goal : To solve the lab, exploit this flaw to bypass the lab's authentication, access the admin interface, and delete the user carlos.

creds : `wiener:peter`

## Analysis

- trying to proceed with role administrator didn't work
- droping the request and accessing home -> makes us proceed with admin privilage ?!!?

## Mitigation

- dont do that
