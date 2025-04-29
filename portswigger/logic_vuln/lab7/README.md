# Lab: Weak isolation on dual-use endpoint

Description : This lab makes a flawed assumption about the user's privilege level based on their input. As a result, you can exploit the logic of its account management features to gain access to arbitrary users' accounts.

End goal : To solve the lab, access the `administrator` account and delete the user `carlos`.

creds : `wiener:peter`

Analysis :

- the application takes the username as an input and compares the current password from the user input with the actual one in the database
- trying several times with wrogn password -> no lock out or any defense mechanism
- so first thing i thought of , i could brute force the admin's password
- but it would take so much time , isn't there anything else i could do ?
  - the answer is yes , i changed the username -> administrator  and removed the current password field
  - the resulted -> password changed successfully!!
  - loged out and  tried to log in as admin -> lab solved!
